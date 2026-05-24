import re
import csv
import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def parse_table_row(line):
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    return cells

def main():
    parser = argparse.ArgumentParser(description="Convert checklist markdown to CSV")
    parser.add_argument("md_file", nargs="?", help="Path to .md file (relative to project root or absolute)")
    args = parser.parse_args()

    if args.md_file:
        md_path = Path(args.md_file)
        if not md_path.is_absolute():
            md_path = BASE_DIR / md_path
    else:
        # Auto-detect: pick the latest .md file in output/
        output_dir = BASE_DIR / "output"
        md_files = sorted(output_dir.glob("Checklist_*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        if not md_files:
            print("ERROR: No Checklist_*.md found in output/")
            sys.exit(1)
        md_path = md_files[0]
        print(f"Auto-detected: {md_path.name}")

    csv_path = md_path.with_suffix(".csv")

    with open(md_path, encoding='utf-8') as f:
        lines = f.readlines()

    rows = []
    current_parent = ""
    current_ticket_key = ""
    current_ticket_title = ""
    current_assignee = ""
    current_status = ""
    current_date = ""
    in_table = False
    header_skipped = False

    for line in lines:
        line = line.rstrip('\n')

        # 親課題 heading
        m = re.match(r'^# 親課題: \[(.+?)\] (.+)', line)
        if m:
            current_parent = f"[{m.group(1)}] {m.group(2)}"
            continue

        # Ticket heading
        m = re.match(r'^## \[(.+?)\] (.+)', line)
        if m:
            current_ticket_key = m.group(1)
            current_ticket_title = m.group(2)
            in_table = False
            header_skipped = False
            continue

        # Metadata lines
        m = re.match(r'^- Người phụ trách: (.+)', line)
        if m:
            current_assignee = m.group(1)
            continue
        m = re.match(r'^- Status: (.+)', line)
        if m:
            current_status = m.group(1)
            continue
        m = re.match(r'^- Ngày comment: (.+)', line)
        if m:
            current_date = m.group(1)
            continue
        m = re.match(r'^- 親課題: (.+)', line)
        if m and not current_parent:
            current_parent = m.group(1)
            continue

        # Table rows
        if line.startswith('|'):
            cells = parse_table_row(line)
            # Skip separator row
            if all(re.match(r'^-+$', c.replace(' ', '')) for c in cells if c):
                header_skipped = True
                in_table = True
                continue
            # Skip header row (first | row before separator)
            if not in_table:
                in_table = True
                continue
            if not header_skipped:
                continue
            if len(cells) >= 8:
                table_cells = (cells + [''] * 9)[:9]  # pad to 9: #,Nhóm,Việc,出典,R1,R2,R3,M,Remark
                rows.append([
                    current_parent,
                    current_ticket_key,
                    current_ticket_title,
                ] + table_cells + [
                    current_assignee,
                    current_status,
                    current_date,
                ])
        else:
            if line.strip() == '' or line.startswith('#') or line.startswith('-'):
                if not line.startswith('|'):
                    in_table = False
                    header_skipped = False

    headers = ['親課題', 'Ticket', 'Tiêu đề màn hình',
               '#', 'Nhóm', 'Việc cần sửa', '出典', 'Round 1', 'Round 2', 'Round 3', 'M', 'Remark',
               'Người phụ trách', 'Status', 'Ngày comment']

    # Pad rows to match headers
    padded_rows = []
    for r in rows:
        while len(r) < len(headers):
            r.append('')
        padded_rows.append(r[:len(headers)])

    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(padded_rows)

    print(f"Done: {len(padded_rows)} rows → {csv_path}")
    return str(csv_path)

if __name__ == '__main__':
    main()
