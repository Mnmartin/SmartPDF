import os
from PyPDF2 import PdfMerger, PdfReader

# specify the directory path where your PDF files are located
pdf_dir = "files"

# create an empty PdfFileMerger object
pdf_merger = PdfMerger()

# loop through the PDF files in the specified directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        # open each PDF file in read-binary mode and add it to the merger object
        with open(os.path.join(pdf_dir, filename), 'rb') as f:
            pdf_merger.append(PdfReader(f))

# write the combined PDF to a file
with open(os.path.join(pdf_dir, "combined.pdf"), "wb") as f:
    pdf_merger.write(f)
