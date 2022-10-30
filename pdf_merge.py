import PyPDF2
import sys

### call this in folder where the pdf files are located ###
### to use with cmd line: python pdf_merge.py <name_of_new_file> <pdf_to_merge_1> <pdf_to_merge_2> ... <pdf_to merge_x> 

merged_pdf = sys.argv[1]
inputs = sys.argv[2:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(merged_pdf)

pdf_combiner(inputs)