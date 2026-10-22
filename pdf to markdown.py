from pypdf import PdfReader

pdf_file = "VEGO GLOBAL EDA Report.pdf"
md_file = "VEGO GLOBAL EDA Report.md"

reader = PdfReader(pdf_file)

with open(md_file, "w", encoding="utf-8") as f:
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        f.write(f"\n\n## Page {page_number}\n\n")
        f.write(text)

print(f"Done: {md_file}")