import torch 
import numpy as np
import torch.nn as nn


def init_seed(reproductivity=True):
    r'''Initialize all the random seeds

    Args: 
    reporductivity:     (bool) enable reproductivity or not

    '''
    np.random.seed(0)
    torch.manual_seed(0)
    torch.cuda.manual_seed_all(0)

    if reproductivity == True:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    else:
        torch.backends.cudnn.deterministic = False
        torch.backends.cudnn.benchmark = True
