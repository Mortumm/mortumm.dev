import PyPDF2
# Requires PyPDF2 -> pip install PyPDF2 

# Combine PDF files
def combine_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfFileMerger()

    for pdf_file in input_pdfs:
        pdf_merger.append(pdf_file)

    pdf_merger.write(output_pdf)
    pdf_merger.close()

# Reorder pages in a PDF
def reorder_pages(input_pdf, output_pdf, page_order):
    pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_number in page_order:
        page = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page)

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

# Usage
if __name__ == "__main__":
    input_pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]
    output_pdf = "combined.pdf"
    page_order = [2, 0, 1]  # Page order through list

    combine_pdfs(input_pdfs, output_pdf)
    reorder_pages(output_pdf, "modified.pdf", page_order)
