import torch.utils.data as data
from abstract_dataloader import AbstractDataLoader

class XXXDataLoader(AbstractDataLoader):
    r'''AbstractDataLoader class 

    Args:
        num_workers:        
        data_set:           (torch.utils.data.Dataset)
        batch_size:

    Outputs:
        Abstract DataLoader
    '''
    def __init__(self, num_workers=0, dataset, batch_size=32):
        super(XXXDataLoader, self).__init__()

    def create_dataloader(self):
        r'''
        create dataloader using self.dataset
        '''
        return DataLoader(self.dataset, batch_size=self.batch_size, num_workers=self.num_workers, shuffle=True)


