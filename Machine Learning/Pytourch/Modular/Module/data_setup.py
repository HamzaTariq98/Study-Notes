import os
import subprocess
import zipfile
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



def data_loaders(ROOT_PATH,BATCH_SIZE, IMAGES_SIZE,P):

    transform = Compose([
        Resize(IMAGES_SIZE),
        ToTensor(),
        Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225]),
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