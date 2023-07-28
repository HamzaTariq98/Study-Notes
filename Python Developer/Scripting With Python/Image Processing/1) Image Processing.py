from PIL import Image, ImageFilter
import os,sys


# Predefined function by help of ChatGPT to return all files name inside a directory
def list_files_in_directory(directory_path):
    files_list = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            files_list.append(filename)
    return files_list


img = Image.open(r'C:\Users\Lenovo\Desktop\Study\GitHub\Python Developer\Scripting With Python\Image Processing\pokemons\charmander.jpg')
filtered_image = img.filter(ImageFilter.FIND_EDGES)
filtered_image.save('Blur.png','png')

img.convert('1').rotate(90).save('convert.png','png')
img.resize((1280,720)).save('i am still here.jpg')


# Change size of image without missup the ratios
img = Image.open(r'C:\Users\Lenovo\Desktop\Study\GitHub\Python Developer\Scripting With Python\Image Processing\pokemons\astro.jpg')
img.thumbnail((400,300))
img.save('modified size image.png','png')








'''
Mini-Project:
convert all files in pokemons from jpg to png
'''

images_file_name = sys.argv[1] # pokemons file images
png_file_name = sys.argv[2] # new directory name



current_path =  os.path.dirname(sys.argv[0])# Finding current path of script
files_in_directory = list_files_in_directory(current_path+r'\\'+images_file_name) # List up all images in pokemons dir


# if dir already exists no need to create it
if not os.path.exists(current_path +'\\'+png_file_name):
    os.mkdir(current_path +'\\'+png_file_name)
new_path_png = current_path + r'\\' + png_file_name

# looping throug all images names and save new images as png
for image in files_in_directory:
    name = image.split('.')[0] # execlude the .jpg part from the name
    img = Image.open(current_path+ r'\\'+ images_file_name + '\\' +image)
    img.save(new_path_png+r'\\'+name+'.png','png')

