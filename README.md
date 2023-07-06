# PDF Splitter, Combiner, and Decrypter

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
This repository contains code for splitting, combining, and decrypting PDF files. The code provides a simple and efficient solution for performing these operations programmatically.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/Mnmartin/SmartPDF.git
   navigate to the project root Directory using CMD
   python -m venv ./env
   env\Scripts\activate
   pip install -r requirement.txt
   
## Usage
1.Splitting PDFs:
  Use the split_pdf.py script to split a PDF file into multiple smaller PDFs based on the desired page ranges or chapter divisions.
  Provide the input PDF file path and specify the desired page ranges or chapters.
2.Combining PDFs:
  Use the combine_pdf.py script to combine multiple PDF files into a single PDF.
  Provide the input PDF file paths in the desired order of combination.
3. Decrypting PDFs:
  Use the decrypt_pdf.py script to remove password protection from encrypted PDF files.
  Provide the input PDF file path and the password for decryption.

## Features
  Split PDF files based on specified page ranges or chapter divisions.
  Combine multiple PDF files into a single PDF.
  Decrypt password-protected PDF files.
## License
This project is licensed under the MIT License.
