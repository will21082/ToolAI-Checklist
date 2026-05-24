#!/usr/bin/env python3
"""
One-command pipeline: detect latest markdown → convert to CSV → upload to Google Sheets.
Usage: python3 scripts/run_all.py [md_file]
"""

import sys
import json
import argparse
from pathlib import Path

# Add scripts dir to path so we can import siblings
sys.path.insert(0, str(Path(__file__).parent))

from md_to_csv import main as convert_md
from upload_to_gdrive import upload_csv_as_sheet

BASE_DIR = Path(__file__).parent.parent
STATE_FILE = BASE_DIR / ".state" / "spreadsheet.json"


def load_spreadsheet_id() -> str | None:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text()).get("spreadsheet_id")
    return None


def save_spreadsheet_id(spreadsheet_id: str, name: str, link: str):
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps({
        "spreadsheet_id": spreadsheet_id,
        "name": name,
        "link": link,
    }, ensure_ascii=False, indent=2))
    print(f"  Đã lưu spreadsheet ID → {STATE_FILE.relative_to(BASE_DIR)}")


def main():
    parser = argparse.ArgumentParser(description="Markdown → CSV → Google Sheets (one command)")
    parser.add_argument("md_file", nargs="?", help="Path to .md file (optional, auto-detects latest)")
    parser.add_argument("--folder-id", help="Google Drive folder ID (optional)")
    parser.add_argument("--spreadsheet-id", help="Override: dùng file Sheets cụ thể (ghi đè config)")
    parser.add_argument("--new-file", action="store_true", help="Bắt buộc tạo file Sheets mới (bỏ qua config)")
    args = parser.parse_args()

    # ── Step 1: Detect markdown file ─────────────────────────────────────────
    if args.md_file:
        md_path = Path(args.md_file)
        if not md_path.is_absolute():
            md_path = BASE_DIR / md_path
    else:
        output_dir = BASE_DIR / "output"
        md_files = sorted(output_dir.glob("Checklist_*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        if not md_files:
            print("ERROR: No Checklist_*.md found in output/")
            sys.exit(1)
        md_path = md_files[0]

    print(f"[1/3] Markdown : {md_path.name}")

    # ── Step 2: Convert .md → .csv ───────────────────────────────────────────
    sys.argv = ["md_to_csv.py", str(md_path)]
    csv_path_str = convert_md()
    print(f"[2/3] CSV      : {Path(csv_path_str).name}")

    # ── Step 3: Resolve spreadsheet ID ───────────────────────────────────────
    if args.new_file:
        spreadsheet_id = None
    elif args.spreadsheet_id:
        spreadsheet_id = args.spreadsheet_id
    else:
        spreadsheet_id = load_spreadsheet_id()
        if spreadsheet_id:
            print(f"[3/3] Thêm tab vào file đã có: {spreadsheet_id}")
        else:
            print(f"[3/3] Chưa có file Sheets → tạo mới")

    # ── Step 4: Upload CSV → Google Sheets ───────────────────────────────────
    file = upload_csv_as_sheet(csv_path_str, folder_id=args.folder_id, spreadsheet_id=spreadsheet_id)

    # Save ID for next run (only when creating a new file or overriding)
    if not spreadsheet_id or args.spreadsheet_id:
        save_spreadsheet_id(file["id"], file["name"], file["webViewLink"])


if __name__ == "__main__":
    main()
