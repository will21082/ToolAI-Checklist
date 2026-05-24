#!/usr/bin/env python3
"""
Upload CSV checklist to Google Sheets with full formatting + checkboxes.
Usage: python3 scripts/upload_to_gdrive.py <csv_file>
"""

import sys
import csv
import argparse
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]
BASE_DIR = Path(__file__).parent.parent
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"

# ── Column indices ────────────────────────────────────────────────────────────
C_PARENT, C_TICKET, C_TITLE          = 0, 1, 2
C_NUM, C_NHOM, C_TASK                = 3, 4, 5
C_R1, C_R2, C_R3, C_M, C_REMARK      = 6, 7, 8, 9, 10
C_ASSIGNEE, C_STATUS, C_DATE         = 11, 12, 13

NCOLS = 14

#                  親課題  Ticket  Tiêu đề  #    Nhóm  Việc   R1   R2   R3   M   Remark  担当  Status  Ngày
COLUMN_WIDTHS_PX = [180,   90,    220,     38,  175,  390,   65,  65,  65,  46,   250,  110,  145,   180]

# ── Colors ───────────────────────────────────────────────────────────────────
def rgb(r, g, b): return {"red": r/255, "green": g/255, "blue": b/255}

HEADER_BG    = rgb(26, 69, 137)   # dark blue
HEADER_FG    = rgb(255, 255, 255) # white
TICKET_A     = rgb(255, 255, 255) # white
TICKET_B     = rgb(241, 245, 253) # very light blue

NHOM_COLORS = {
    "Header & Navigation":                      rgb(207, 226, 255),
    "UI Components & Controls":                 rgb(198, 239, 206),
    "Hiển thị & Đồng bộ Thông tin":             rgb(255, 249, 196),
    "Cấu trúc Layout & Vị trí Thông tin":       rgb(255, 235, 205),
    "Screen Flow & Luồng Xử lý":                rgb(234, 209, 252),
    "Input Fields & Form Design":               rgb(252, 213, 226),
    "Tab & Thông tin Chi tiết / Consistency":   rgb(200, 245, 250),
    "Visual Style":                             rgb(252, 210, 210),
    "Data Format":                              rgb(230, 230, 230),
}


def get_credentials():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return creds


def analyze_csv(csv_path: Path):
    """Return ticket groups, parent groups, nhom cells, and total row count."""
    rows = []
    with open(csv_path, encoding="utf-8-sig") as f:
        for i, row in enumerate(csv.reader(f)):
            rows.append(row)

    ticket_groups = []   # (start_row_1based, end_row_1based, ticket_key)
    parent_groups = []   # (start_row_1based, end_row_1based, parent_key)
    nhom_cells = []      # (row_1based, nhom_value)

    current_ticket = None
    current_parent = None
    ticket_start = 2
    parent_start = 2

    for i, row in enumerate(rows[1:], start=2):
        ticket = row[C_TICKET] if len(row) > C_TICKET else ""
        parent = row[C_PARENT] if len(row) > C_PARENT else ""
        nhom   = row[C_NHOM]   if len(row) > C_NHOM   else ""

        if ticket != current_ticket:
            if current_ticket is not None:
                ticket_groups.append((ticket_start, i - 1, current_ticket))
            current_ticket = ticket
            ticket_start = i

        if parent != current_parent:
            if current_parent is not None:
                parent_groups.append((parent_start, i - 1, current_parent))
            current_parent = parent
            parent_start = i

        nhom_cells.append((i, nhom))

    if current_ticket:
        ticket_groups.append((ticket_start, len(rows), current_ticket))
    if current_parent:
        parent_groups.append((parent_start, len(rows), current_parent))

    return ticket_groups, parent_groups, nhom_cells, len(rows)


def format_sheet(sheets_svc, spreadsheet_id, csv_path: Path, sheet_id: int = None):
    ticket_groups, parent_groups, nhom_cells, total_rows = analyze_csv(csv_path)

    if sheet_id is not None:
        sid = sheet_id
    else:
        meta = sheets_svc.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sid = meta["sheets"][0]["properties"]["sheetId"]

    def cell_range(r1, r2, c1, c2):
        return {"sheetId": sid, "startRowIndex": r1-1, "endRowIndex": r2,
                "startColumnIndex": c1, "endColumnIndex": c2}

    requests = []

    # ── 1. Freeze header row + 3 columns (親課題, Ticket, Tiêu đề) ────────────
    requests.append({"updateSheetProperties": {
        "properties": {"sheetId": sid, "gridProperties": {
            "frozenRowCount": 1, "frozenColumnCount": 3}},
        "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount"
    }})

    # ── 2. Header row — bold, dark blue bg, white text, center ───────────────
    requests.append({"repeatCell": {
        "range": cell_range(1, 1, 0, NCOLS),
        "cell": {"userEnteredFormat": {
            "backgroundColor": HEADER_BG,
            "textFormat": {"bold": True, "fontSize": 10,
                           "foregroundColor": HEADER_FG},
            "horizontalAlignment": "CENTER",
            "verticalAlignment": "MIDDLE",
            "wrapStrategy": "WRAP",
        }},
        "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
    }})

    # ── 3. All data cells — base style ───────────────────────────────────────
    requests.append({"repeatCell": {
        "range": cell_range(2, total_rows, 0, NCOLS),
        "cell": {"userEnteredFormat": {
            "textFormat": {"fontSize": 10},
            "verticalAlignment": "TOP",
            "borders": {
                "top":    {"style": "SOLID", "color": rgb(200,200,200)},
                "bottom": {"style": "SOLID", "color": rgb(200,200,200)},
                "left":   {"style": "SOLID", "color": rgb(200,200,200)},
                "right":  {"style": "SOLID", "color": rgb(200,200,200)},
            }
        }},
        "fields": "userEnteredFormat(textFormat,verticalAlignment,borders)"
    }})

    # ── 4. Wrap text — Nhóm, Việc cần sửa, Remark ───────────────────────────
    for col in (C_NHOM, C_TASK, C_REMARK):
        requests.append({"repeatCell": {
            "range": cell_range(2, total_rows, col, col+1),
            "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
            "fields": "userEnteredFormat.wrapStrategy"
        }})

    # ── 5. Center align — #, Round 1/2/3, M ─────────────────────────────────
    requests.append({"repeatCell": {
        "range": cell_range(2, total_rows, C_NUM, C_NUM+1),
        "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
        "fields": "userEnteredFormat.horizontalAlignment"
    }})
    requests.append({"repeatCell": {
        "range": cell_range(2, total_rows, C_R1, C_M+1),
        "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
        "fields": "userEnteredFormat.horizontalAlignment"
    }})

    # ── 6. Column widths ──────────────────────────────────────────────────────
    for col, px in enumerate(COLUMN_WIDTHS_PX):
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": col, "endIndex": col+1},
            "properties": {"pixelSize": px},
            "fields": "pixelSize"
        }})

    # ── 7. Row height for header ──────────────────────────────────────────────
    requests.append({"updateDimensionProperties": {
        "range": {"sheetId": sid, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
        "properties": {"pixelSize": 36},
        "fields": "pixelSize"
    }})

    # ── 8. Checkboxes — Round 1, Round 2, Round 3 ────────────────────────────
    requests.append({"setDataValidation": {
        "range": cell_range(2, total_rows, C_R1, C_R3+1),
        "rule": {
            "condition": {"type": "BOOLEAN"},
            "strict": True,
            "showCustomUi": True,
        }
    }})

    # ── 9. Ticket alternating row colors ─────────────────────────────────────
    for idx, (start, end, _) in enumerate(ticket_groups):
        bg = TICKET_B if idx % 2 == 0 else TICKET_A
        requests.append({"repeatCell": {
            "range": cell_range(start, end, 0, NCOLS),
            "cell": {"userEnteredFormat": {"backgroundColor": bg}},
            "fields": "userEnteredFormat.backgroundColor"
        }})

    # ── 10. Nhóm column — color by category ──────────────────────────────────
    for row_idx, nhom in nhom_cells:
        color = NHOM_COLORS.get(nhom)
        if color:
            requests.append({"repeatCell": {
                "range": cell_range(row_idx, row_idx, C_NHOM, C_NHOM+1),
                "cell": {"userEnteredFormat": {"backgroundColor": color}},
                "fields": "userEnteredFormat.backgroundColor"
            }})

    # ── 11. Conditional formatting — M column (red bg when not blank) ────────
    requests.append({"addConditionalFormatRule": {
        "rule": {
            "ranges": [cell_range(2, total_rows, C_M, C_M+1)],
            "booleanRule": {
                "condition": {"type": "NOT_BLANK"},
                "format": {"backgroundColor": rgb(255, 153, 153)},
            }
        },
        "index": 0
    }})

    # ── 12. Conditional formatting — # column bold when = 1 ──────────────────
    requests.append({"addConditionalFormatRule": {
        "rule": {
            "ranges": [cell_range(2, total_rows, C_NUM, C_NUM+1)],
            "booleanRule": {
                "condition": {"type": "NUMBER_EQ", "values": [{"userEnteredValue": "1"}]},
                "format": {"textFormat": {"bold": True}},
            }
        },
        "index": 1
    }})

    # ── 13. Outer border for entire table ─────────────────────────────────────
    requests.append({"updateBorders": {
        "range": cell_range(1, total_rows, 0, NCOLS),
        "top":    {"style": "SOLID_MEDIUM", "color": rgb(26, 69, 137)},
        "bottom": {"style": "SOLID_MEDIUM", "color": rgb(26, 69, 137)},
        "left":   {"style": "SOLID_MEDIUM", "color": rgb(26, 69, 137)},
        "right":  {"style": "SOLID_MEDIUM", "color": rgb(26, 69, 137)},
    }})

    # ── 14. Merge cells by ticket: Ticket, Tiêu đề, Người phụ trách, Status, Ngày ──
    for start, end, _ in ticket_groups:
        if end > start:
            for col in (C_TICKET, C_TITLE, C_ASSIGNEE, C_STATUS, C_DATE):
                requests.append({"mergeCells": {
                    "range": cell_range(start, end, col, col+1),
                    "mergeType": "MERGE_ALL"
                }})

    # ── 15. Merge cells by 親課題 ─────────────────────────────────────────────
    for start, end, _ in parent_groups:
        if end > start:
            requests.append({"mergeCells": {
                "range": cell_range(start, end, C_PARENT, C_PARENT+1),
                "mergeType": "MERGE_ALL"
            }})

    # ── 16. MIDDLE + CENTER align for merged columns ──────────────────────────
    for col in (C_PARENT, C_TICKET, C_TITLE, C_ASSIGNEE, C_STATUS, C_DATE):
        requests.append({"repeatCell": {
            "range": cell_range(2, total_rows, col, col+1),
            "cell": {"userEnteredFormat": {
                "verticalAlignment": "MIDDLE",
                "horizontalAlignment": "CENTER",
                "wrapStrategy": "WRAP",
            }},
            "fields": "userEnteredFormat(verticalAlignment,horizontalAlignment,wrapStrategy)"
        }})

    # ── Send all requests ─────────────────────────────────────────────────────
    sheets_svc.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"requests": requests}
    ).execute()

    merge_count = sum(1 for s, e, _ in ticket_groups if e > s) * 5 + sum(1 for s, e, _ in parent_groups if e > s)
    print(f"  Formatting applied: {len(ticket_groups)} ticket groups, {len(nhom_cells)} data rows, {merge_count} merges")


def add_sheet_to_existing(sheets_svc, spreadsheet_id: str, sheet_name: str, csv_path: Path):
    """Add a new tab to an existing spreadsheet, write CSV data, then format it."""

    # Read CSV data
    rows = []
    with open(csv_path, encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            rows.append(row)

    # Delete existing tab with same name if present
    meta = sheets_svc.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    existing = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}
    if sheet_name in existing:
        sheets_svc.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"requests": [{"deleteSheet": {"sheetId": existing[sheet_name]}}]}
        ).execute()
        print(f"  Tab '{sheet_name}' đã tồn tại → xóa và tạo lại")

    # Add new sheet tab
    add_resp = sheets_svc.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"requests": [{"addSheet": {"properties": {"title": sheet_name}}}]}
    ).execute()
    sid = add_resp["replies"][0]["addSheet"]["properties"]["sheetId"]

    # Write CSV data to the new sheet
    sheets_svc.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"'{sheet_name}'!A1",
        valueInputOption="RAW",
        body={"values": rows}
    ).execute()

    print(f"  Tab '{sheet_name}' created → formatting...")
    format_sheet(sheets_svc, spreadsheet_id, csv_path, sheet_id=sid)

    link = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={sid}"
    return {"id": spreadsheet_id, "name": sheet_name, "webViewLink": link}


def upload_csv_as_sheet(csv_path: str, folder_id: str = None, spreadsheet_id: str = None):
    csv_path = Path(csv_path)
    if not csv_path.is_absolute():
        csv_path = BASE_DIR / csv_path
    if not csv_path.exists():
        print(f"ERROR: File not found: {csv_path}")
        sys.exit(1)

    print(f"Uploading: {csv_path.name}")
    creds = get_credentials()

    sheets_svc = build("sheets", "v4", credentials=creds)

    # ── Mode A: add new tab to existing spreadsheet ───────────────────────────
    if spreadsheet_id:
        sheet_name = csv_path.stem
        file = add_sheet_to_existing(sheets_svc, spreadsheet_id, sheet_name, csv_path)
        print(f"\n✓ Hoàn tất!")
        print(f"  Tab mới  : {file['name']}")
        print(f"  Link mở  : {file['webViewLink']}")
        return file

    # ── Mode B: create new spreadsheet file ───────────────────────────────────
    drive_svc = build("drive", "v3", credentials=creds)

    metadata = {
        "name": csv_path.stem,
        "mimeType": "application/vnd.google-apps.spreadsheet",
    }
    if folder_id:
        metadata["parents"] = [folder_id]

    media = MediaFileUpload(str(csv_path), mimetype="text/csv", resumable=True)
    file = drive_svc.files().create(
        body=metadata, media_body=media, fields="id,name,webViewLink"
    ).execute()

    print(f"  Uploaded → formatting...")
    format_sheet(sheets_svc, file["id"], csv_path)

    print(f"\n✓ Hoàn tất!")
    print(f"  Tên file : {file['name']}")
    print(f"  Link mở  : {file['webViewLink']}")
    return file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="Path to CSV file")
    parser.add_argument("--folder-id", help="Google Drive folder ID (optional)")
    parser.add_argument("--spreadsheet-id", help="Existing spreadsheet ID — adds new tab instead of creating new file")
    args = parser.parse_args()
    upload_csv_as_sheet(args.csv_file, args.folder_id, args.spreadsheet_id)


if __name__ == "__main__":
    main()
