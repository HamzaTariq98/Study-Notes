import pdb
import os
# Good library for building softwares compatible with variety of OS (Windows, Mac ...)
from pathlib import Path
from translate import Translator


print(os.getcwd())

file_path = 'C:\\Users\\Lenovo\\Desktop\\Study\\GitHub\\Python Developer\\text.txt'
my_file = open(file_path)

# to automatically close the file, using std way:
# write mode also create new files if they doesn't exist
with open(file_path, mode='w') as my_file:
    text = ('helloooooooooooo\n')
    for i in range(10):
        my_file.write(str(i+1)+') '+text)
    # my_file.seek(0)

try:
    with open(file_path, mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("file not found...")

with open(file_path, mode='a') as my_file:
    my_file.write('\n')
    my_file.write('Appended text')

path = 'a new file.txt'


# Using Relative Paths to access files
new_cwd = r'C:\Users\Lenovo\Desktop\Study\GitHub\Python Developer'
os.chdir(new_cwd)
with open(r'New\\'+path) as my_file:
    print(my_file.read())


# Common way of handling file not found error in read mode ==> 'file not found...'
try:
    with open(file_path+'fdfdf', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("file not found...")


# Also common files Error Handling method is IOError, ex if mode in invalid
try:
    with open(file_path, mode='x') as my_file:
        print(my_file.read())
except IOError:
    print("IOError")

# Read text we want to translate
text = ''
with open('translate me.txt', encoding= 'utf-8') as text_file:
    text = text_file.read()

# Translate text
language = 'ar'
translator = Translator(to_lang=language)
text = translator.translate(text)
# Write translation text into new file
with open(f'translation for {language}.txt', encoding= 'utf-8', mode = 'w') as text_file:
    text_file.write(text)
print(text)