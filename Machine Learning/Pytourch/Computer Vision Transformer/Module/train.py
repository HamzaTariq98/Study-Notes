import torch
import argparse
from pathlib import Path
from torchsummary import summary

from model_builder import Model
from engine import test_step, train_step
from data_setup import data_loaders
from utils import save_model





def model_training(
        P,
        EMBEDDING_LENGTH,
        EPOCHS,
        BATCH_SIZE,
        HIDDEN_UNITS,
        IMAGES_SIZE,
        MODEL_NAME,
        ROOT_PATH
):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cpu')

    train_data, test_data, class_names = data_loaders(ROOT_PATH=ROOT_PATH,BATCH_SIZE=BATCH_SIZE,IMAGES_SIZE=IMAGES_SIZE,P=P)

    sample = next(iter(train_data))
    sample,label = sample[0][0],sample[1][0]
    print(f'label is {label}')
    print(f'Sample shape of {sample.shape}==>\n',sample)
    


    model = Model(HIDDEN_UNITS,P,EMBEDDING_LENGTH,IMAGES_SIZE)
    model = model.to(device)

    with torch.inference_mode():
        embd = model(sample)
        print(f'run through Embedding shape {embd.shape}\n{embd}')
    print(sample.shape)
    summary(model,(400,675))

    return None


    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())

    for epoch in range(EPOCHS):
        train_step(
            epoch,
            model,
            loss_fn,
            optimizer,
            train_data,
            device
            )

        acc = test_step(
            epoch,
            model,
            loss_fn,
            test_data,
            device
        )


    save_model(model,path = ROOT_PATH ,MODEL_NAME = MODEL_NAME + f'{int(HIDDEN_UNITS)}-units {int(acc*100//1)}%')



if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Train a model with specified parameters.')
    

    
    parser.add_argument('--P', type=int, default=15)
    parser.add_argument('--EMBEDDING_LENGTH', type=int, default=25)
    parser.add_argument('--epochs', type=int, default=3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--hidden_units', type=int, default=30)
    parser.add_argument('--images_size', type=int, nargs=2, default=(300,300))
    parser.add_argument('--model_name', type=str, default='Eff NetB0')
    parser.add_argument('--root_path', type=str, default='/home/hamza/Desktop/Study-Notes/Machine Learning/Pytourch/Modular')

    args = parser.parse_args()

    EPOCHS = args.epochs
    EMBEDDING_LENGTH = args.EMBEDDING_LENGTH
    BATCH_SIZE = args.batch_size
    HIDDEN_UNITS = args.hidden_units
    IMAGES_SIZE = args.images_size
    MODEL_NAME = args.model_name
    P = args.P
    ROOT_PATH = Path(args.root_path)


    model_training(
        P,
        EMBEDDING_LENGTH,
        EPOCHS,
        BATCH_SIZE,
        HIDDEN_UNITS,
        IMAGES_SIZE,
        MODEL_NAME,
        ROOT_PATH
    )
