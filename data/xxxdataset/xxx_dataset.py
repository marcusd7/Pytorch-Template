import torch
import os
import numpy as np
import pandas as pd
import torch.utils.data as data
from abstract_dataset import AbstractDataSet
from sklearn.model_selection import train_test_split


class XXXDataSet(AbstractDataSet):
    r'''AbstractDataSet class 

    Args:
        data_dir:           (str) directory of xxxdataset, 
                            e.g. data/xxxdataset/xxx_raw_data
        file_list_type:     (str) type of the file list of collected raw dataset, 
                            could be csv...(csv, json)
        file_list_type:     (str) file name of the file list, default to be 'file_list'
        test_size:          (float/double) test dataset size used to separate dataset,
                            default to be 0.2

    Outputs:
        Abstract Dataset class which could be inherited by specified dataset
    '''

    def __init__(self, data_dir, file_list_type, file_list_name = r'file_list', test_size=0.2):
        super(XXXDataSet, self).__init__()

    def _load_file_list(self):
        r'''
        load training & testing file list
        '''
        if self.file_list_type == r'csv':
            file_list_path = os.path.join(self.data_dir, self.file_list_name + r'.csv')
            self.file_list = np.array(pd.read_csv(file_list_path, header=None))

    def _train_test_separation(self):
        r'''
        separate training and test dataset
        '''
        train_list, test_list = train_test_split(
            self. file_list, test_size=self.test_size, random_state=0)
        return train_list, test_list

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        item = self.file_list[idx]
        return item