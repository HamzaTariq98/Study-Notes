import PyPDF2
import os,sys
import pdb
from pathlib import Path

current_path =  os.path.dirname(sys.argv[0])# Finding current path of script
os.chdir(current_path) # change cwd for desired path as in VScode cwd in desktop

script_path = Path(__file__).parent

file_name = 'twopage.pdf'
with open(file_name,'rb') as pdf:
    reader = PyPDF2.PdfFileReader(pdf)
    new_page = reader.getPage(0).rotateClockwise(90) # define a page (first page + rotate 90 degree)
    writer = PyPDF2.PdfFileWriter() # define PDF file writer object to store new pdfs inside machine
    writer.addPage(new_page) # cast new_page into the object


    new_file_name = 'my_new_pdf.pdf'
    with open(new_file_name,'wb') as new_pdf:
        writer.write(new_pdf) 




'''

Mini Project:
Union PDF pages

'''

pdf_file_name = '1) PDF to merge'
output_file_name = '2) Merged PDF output'

# Predefined function by help of ChatGPT to return all pdf files inside a directory
def list_pdf_in_directory(directory_path):   
    pdf_files_names = [filename for filename in os.listdir(directory_path) if filename.lower().endswith('.pdf')]
    os.chdir(f'{current_path}\\{directory_path}') 
    pdf_files = [open(pdf_name, 'rb') for pdf_name in pdf_files_names]
    os.chdir(current_path)
    return pdf_files


def combine_pdf_pages(*arg):

    merger = PyPDF2.PdfFileMerger()
    for pdf_file in arg[0]:
        print(pdf_file)
        merger.append(pdf_file)

    if not os.path.exists(output_file_name):
        os.mkdir(output_file_name)
    with open(f'{output_file_name}\\output.pdf','wb') as output:
        merger.write(output)



pdf_list = list_pdf_in_directory(pdf_file_name) # List up pdf objects using predefined function
combine_pdf_pages(pdf_list)














