from torch import nn
from torch.nn.modules import Module, Sequential



class Model(Module):
    def __init__(self,HIDDEN_UNITS,P,EMBEDDING_LENGTH,IMAGES_SIZE):
        super().__init__()
        N = IMAGES_SIZE[0]**2//P**2
        self.seq = Sequential(
            nn.Embedding(256,EMBEDDING_LENGTH),
            # nn.LSTM([N,P**2*3],HIDDEN_UNITS)
        )


    def forward(self,x):
        return self.seq(x)

