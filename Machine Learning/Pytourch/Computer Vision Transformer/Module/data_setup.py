import os
import subprocess
import zipfile
import numpy as np
import torch
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor,Compose, Resize,Normalize 


num_workers = os.cpu_count()


def data_installing(ROOT_PATH, DATA_FILE_ID = '1yIhmdZRwcvyWOl92PygSVGSualOxiwjg'):
    
    url = f'https://docs.google.com/uc?export=download&id={DATA_FILE_ID}'
    output_file = 'data.zip'
    output_path = ROOT_PATH / 'Data' / output_file

    command = ['wget', '--no-check-certificate', url, '-O', output_path]

    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with zipfile.ZipFile(output_path,'r') as zip:
        zip.extractall(output_path.parent)

    os.remove(output_path)
    print('Data loaded..')




class ImageSlicer:
    def __init__(self,P,IMAGES_SIZE):
        self.P = P
        self.IMAGES_SIZE = IMAGES_SIZE

    def __call__(self,img):
     return image_slicer(img,self.P,self.IMAGES_SIZE)



def image_slicer(img,P,IMAGES_SIZE):
        img = np.array(img)
        N = IMAGES_SIZE[0]**2//P**2
        patches = []
        for n in range(N):
            x,y = divmod(n,IMAGES_SIZE[0]//P)


            x_start = x*P
            x_end = (x+1)*P
            y_start = y*P
            y_end = (y+1)*P
            patch = img[x_start:x_end,y_start:y_end,:]
            patch = torch.tensor(patch)
            patch = patch.reshape(-1)
            # print(patch)
            # patch = torch.concatenate([patch,torch.tensor([x,y])])
            patches.append(patch)

        patches = torch.tensor(np.array(patches),dtype=torch.long)
        return patches



def data_loaders(ROOT_PATH,BATCH_SIZE, IMAGES_SIZE,P):



    transform = Compose([
        Resize(IMAGES_SIZE),
        # ToTensor(),
        # Normalize(mean=[0.485, 0.456, 0.406],
        #                     std=[0.229, 0.224, 0.225]),
        ImageSlicer(P,IMAGES_SIZE),
    ])

    train_data = ImageFolder(ROOT_PATH / 'Data' / 'Training_data',
                            transform=transform)
   
    test_data = ImageFolder(ROOT_PATH / 'Data' / 'Test_data',
                            transform=transform)

    train_data_ = DataLoader(train_data,batch_size = BATCH_SIZE, shuffle=True, num_workers=num_workers)
    test_data_ = DataLoader(test_data, batch_size=BATCH_SIZE,num_workers=num_workers)

    class_names = train_data.classes


    return train_data_,test_data_, class_names


if __name__=='__main__':
    data_installing(Path('/home/hamza/Desktop/Study-Notes/Machine Learning/Pytourch/Modular'))