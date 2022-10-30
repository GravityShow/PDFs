import PyPDF2
import sys

# input_pdf = sys.argv[1]
# watermark = sys.argv[2]
# result = sys.argv[3]

### call this in folder where the pdf files are located ###
### to use with cmd line: python pdf_watermark.py <name_of_pdf_file> <name_of_pdf_watermark_source> <name_of_output_pdf_file>

input_pdf = PyPDF2.PdfFileReader(open(sys.argv[1], "rb"))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))

output = PyPDF2.PdfFileWriter()

for i in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open(sys.argv[3], "wb") as file:
        output.write(file)
        