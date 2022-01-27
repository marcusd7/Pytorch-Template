import torch
import torch.nn as nn
from torch.nn import functional as F

class AbstractModel(nn.Module):

    def __init__(self, model):
        super(AbstractModel,self).__init__()
        self.model = model
    
    def forward(self):
        r'''
        computed the foward loss of the model
        '''
        raise NotImplementedError

    