from pypdf import PdfReader

pdf_path = "test.pdf"
reader = PdfReader(pdf_path)

#print(f"Number of pages: {len(reader.pages)}")
#can also print number of pages if needed

page = reader.pages[0]
text = page.extract_text()
print(text)
