import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_group(input_path, output_path, page_groups):
    # Open the PDF file
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PdfReader(input_file)
        # Get the total number of pages in the PDF
        total_pages = len(pdf_reader.pages)

        # Loop through each group of pages
        for i, page_range in enumerate(page_groups):
            # Create a new PDF writer object for each group
            pdf_writer =PdfWriter()
            # Loop through each page in the group
            for page_num in range(page_range[0]-1, page_range[1]):
                # Add the current page to the writer
                pdf_writer.add_page(pdf_reader.pages[page_num])
            # Save the output to a new file with the group number as the name
            output_file_path = os.path.join(output_path, f"group_{i+1}.pdf")
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)

if __name__ == '__main__':
    # Example usage: split pages 1-3 of input.pdf and save to output directory
    input_path = 'file.pdf'
    output_path = 'output'
    page_groups = [(1,48), (49, 62), (63, 83)] # split the PDF into three groups of 5 pages each
    split_pdf_by_group(input_path, output_path, page_groups)
