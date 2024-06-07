import torch
from sklearn.metrics import accuracy_score




def train_step(
    epoch,
    model,
    loss_fn,
    optimizer,
    train_data,
    device):

    train_loss, train_acc = 0,0
    for batch, (X,y) in enumerate(train_data):
        X,y = X.to(device), y.to(device)
        model.train()
        optimizer.zero_grad()

        y_pred = model(X)
        loss = loss_fn(y_pred,y)
        train_loss+= loss
        train_acc += accuracy_score(torch.softmax(y_pred,dim=1).argmax(axis=1).cpu(),y.cpu())

        loss.backward()
        optimizer.step()

    train_loss /= len(train_data)
    train_acc /= len(train_data)
    print(f'Epoch {epoch} | train_Loss {train_loss:.2f} | train_acc {train_acc:.2f}')


def test_step(
    epoch,
    model,
    loss_fn,
    test_data,
    device):
    
  
    
    model.eval()
    with torch.inference_mode():
        test_loss, test_acc = 0,0
        for _, (X,y) in enumerate(test_data):
            X,y = X.to(device), y.to(device)
            y_pred = model(X)
            test_loss += loss_fn(y_pred,y)
            test_acc += accuracy_score(torch.softmax(y_pred,dim=1).argmax(axis=1).cpu(),y.cpu())

            test_loss /= len(test_data)
            test_acc /= len(test_data)
        print(f'Epoch {epoch} | test_loss {test_loss:.2f} | test_acc {test_acc:.2f}')
    return test_acc
