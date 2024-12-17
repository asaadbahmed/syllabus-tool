from pypdf import PdfReader

# we would want to clone the file, but since we are just reading the file & this is just the testing phase it doesn't matter
reader = PdfReader("Sample Outline.pdf")

if len(reader.pages) > 15:
    raise Exception("Please provide a PDF that has less than or equal to 15 pages.")

# try using fuzzywuzzy instead?
for pageNumber, page in enumerate(reader.pages):
    page_text = page.extract_text()
    compressed_text = page_text.lower().replace(" ", "").replace("\n", "").replace("\r", "")
    found_course_eval = compressed_text.find("courseevaluation")
    
    if found_course_eval == -1:
        continue

    print(f"Found course evaluation on: {pageNumber + 1}")
    relevantText = page_text[found_course_eval:]
    print(relevantText)
    break