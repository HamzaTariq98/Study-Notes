import torch
import numpy as np
from torch import nn
from torch.nn.modules import Module


POS_EMBED_LENGHT = 12



def create_qkv(x,d_model,num_head):
    qvk = x.reshape((x.shape[0],x.shape[1],num_head,3*d_model//num_head))
    qvk = qvk.permute(0,2,1,3)
    print(qvk.shape)
    q,v,k = qvk.chunk(3,axis=-1)
    return q,v,k



class Block_1(Module):
    def __init__(self,N,EMBEDDING_LENGTH,d_model,num_head):
        super().__init__()
        self.d_model = d_model
        self.num_head = num_head
        self.norm_1 = nn.LayerNorm((N,EMBEDDING_LENGTH + POS_EMBED_LENGHT))
        self.multi_head_attention = nn.MultiheadAttention(EMBEDDING_LENGTH + POS_EMBED_LENGHT,num_head,batch_first=True)

    def forward(self,x):
        x = self.norm_1(x)
        x,_ = self.multi_head_attention(x,x,x,need_weights = False)
        return x
    



class Block_2(Module):
    def __init__(self,N,EMBEDDING_LENGTH):
        super().__init__()
        self.norm_2 = nn.LayerNorm((N, EMBEDDING_LENGTH + POS_EMBED_LENGHT))
        self.MLP = nn.Sequential(
            nn.Linear(EMBEDDING_LENGTH + POS_EMBED_LENGHT,EMBEDDING_LENGTH + POS_EMBED_LENGHT),
            nn.ReLU()
        )

    def forward(self,x):
        x = self.norm_2(x)
        x = self.MLP(x)
        return x
    


class Transformer(Module):
    def __init__(self,N,EMBEDDING_LENGTH,d_model,num_head):
        super().__init__()
        self.block_1 = Block_1(N,EMBEDDING_LENGTH,d_model,num_head)
        self.block_2 = Block_2(N,EMBEDDING_LENGTH)
    def forward(self,x):
        x = self.block_1(x) + x
        x = self.block_2(x) + x
        return x




class Model(Module):
    def __init__(self,HIDDEN_UNITS,P,EMBEDDING_LENGTH,IMAGES_SIZE,BATCH_SIZE,d_model,num_head,L):
        super().__init__()
        self.N = IMAGES_SIZE[0]**2//P**2
        self.EMBEDDING_LENGTH = EMBEDDING_LENGTH
        self.d_model = d_model
        self.num_head = num_head
        self.conv = nn.Conv2d(3,EMBEDDING_LENGTH,(P,P),(P,P))

        self.posEmbed = nn.Embedding(self.N,POS_EMBED_LENGHT)
        
        self.tranformers = nn.ModuleList([Transformer(self.N,EMBEDDING_LENGTH,d_model,num_head) for _ in range(L)])
        
        self.mlp_head = nn.Sequential(
            nn.Linear(EMBEDDING_LENGTH + POS_EMBED_LENGHT,EMBEDDING_LENGTH + POS_EMBED_LENGHT),
            nn.ReLU()
        )

        self.flat = nn.AdaptiveMaxPool2d((1,EMBEDDING_LENGTH + POS_EMBED_LENGHT))

        self.output = nn.Linear(EMBEDDING_LENGTH + POS_EMBED_LENGHT,10)
        


    def forward(self,x):
        x = self.conv(x)
        x = torch.permute(x,(0,1,3,2))
        x = x.reshape((-1,self.N,self.EMBEDDING_LENGTH))
        print(f'x shape {x.shape}')

        token_embedding = torch.arange(self.N)
        posEmbed = self.posEmbed(token_embedding)
        posEmbed = posEmbed.unsqueeze(0).repeat((x.shape[0],1,1))


        x = torch.cat([x,posEmbed],axis=-1)
        print(f'Adding posEmb {x.shape}')



        for trans in self.tranformers:
            x = trans(x)
        print(f'Transformer output {x.shape}')

        x = self.mlp_head(x)
        print(f'MLP output x {x.shape}')

        x = self.flat(x)
        x =x.view(x.size(0), -1)
        print(f'Flatten x {x.shape}')

        x = self.output(x)
        print(f'Final output x {x.shape}')

        return x

