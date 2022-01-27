import torch.utils.data as data

class AbstractDataLoader(data.DataLoader):
    r'''AbstractDataLoader class 

    Args:
        num_workers:        
        data_set:           (torch.utils.data.Dataset)
        batch_size:

    Outputs:
        Abstract DataLoader
    '''
    def __init__(self, num_workers=0, dataset, batch_size=32):
        super().__init__()
        self.num_workers = num_workers
        self.dataset = dataset
        self.batch_size = batch_size

    def create_dataloader(self):
        r'''
        create dataloader using self.dataset
        '''
        return DataLoader(self.dataset, batch_size=self.batch_size, num_workers=self.num_workers, shuffle=True)


