from torch import nn
import torchvision
from torch.nn.modules import Module, Sequential


class FullyDensed(Module):
    def __init__(self,HIDDEN_UNITS):
        super().__init__()

        # weights = torchvision.models.EfficientNet_V2_S_Weights.DEFAULT
        # model = torchvision.models.efficientnet_v2_s(weights=weights)
        
        # for param in model.features.parameters():
        #    param.requires_grad = False
        # model.classifier[1] = nn.Linear(1280,10)
        
        
        weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
        model = torchvision.models.efficientnet_b0(weights=weights)

        for param in model.features.parameters():
            param.requires_grad = False
        model.classifier[1] = nn.Linear(1280,10)


        self.seq = Sequential(
            # nn.Conv2d(3,HIDDEN_UNITS,3),
            # nn.Conv2d(HIDDEN_UNITS,HIDDEN_UNITS,3),
            # nn.ReLU(),
            # nn.MaxPool2d(2,2),
            # nn.Conv2d(HIDDEN_UNITS,HIDDEN_UNITS,3),
            # nn.Conv2d(HIDDEN_UNITS,50,3),
            # nn.ReLU(),
            # nn.MaxPool2d(2,2),
            # nn.Flatten(),
            # nn.Linear(800,10)
            model,
        )

    def forward(self,x):
        return self.seq(x)

