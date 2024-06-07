import torch


def save_model(model,path,MODEL_NAME):
    MODEL_NAME = MODEL_NAME + '.pth'
    SAVED_MODEL_PATH = path / 'Models' / MODEL_NAME
    torch.save(model,f=SAVED_MODEL_PATH)

    