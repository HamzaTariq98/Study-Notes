import torch
import argparse
from pathlib import Path

from model_builder import FullyDensed
from engine import test_step, train_step
from data_setup import data_loaders
from utils import save_model





def model_training(
        EPOCHS,
        BATCH_SIZE,
        HIDDEN_UNITS,
        IMAGES_SIZE,
        MODEL_NAME,
        ROOT_PATH
):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cpu')

    train_data, test_data, class_names = data_loaders(ROOT_PATH=ROOT_PATH,BATCH_SIZE=BATCH_SIZE,IMAGES_SIZE=IMAGES_SIZE)

    
    model = FullyDensed(HIDDEN_UNITS)
    model = model.to(device)

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
    
    parser.add_argument('--epochs', type=int, default=3, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    parser.add_argument('--hidden_units', type=int, default=30, help='Number of hidden units')
    parser.add_argument('--images_size', type=int, nargs=2, default=[300,300], help='Size of the images')
    parser.add_argument('--model_name', type=str, default='Eff NetB0', help='Name of the model')
    parser.add_argument('--root_path', type=str, default='/home/hamza/Desktop/Study-Notes/Machine Learning/Pytourch/Modular', help='Root path')

    args = parser.parse_args()

    EPOCHS = args.epochs
    BATCH_SIZE = args.batch_size
    HIDDEN_UNITS = args.hidden_units
    IMAGES_SIZE = args.images_size
    MODEL_NAME = args.model_name
    ROOT_PATH = Path(args.root_path)


    model_training(
        EPOCHS,
        BATCH_SIZE,
        HIDDEN_UNITS,
        IMAGES_SIZE,
        MODEL_NAME,
        ROOT_PATH
    )
