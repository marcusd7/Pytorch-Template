import torch
import os
import numpy as np
import pickle as pkl
import torch.utils.data as data

from torchvision import transforms
from sklearn.model_selection import train_test_split


class AbstractDataSet(data.Dataset):
    '''AbstractDataSet class 
    Args:
    Outputs:
    '''

    def __init__(self, data_dir):

        self.data_dir = data_dir
        self._check_files()

    def _check_files(self):
        # This part is the core code block for load your own dataset.
        # You can choose to scan a folder, or load a file list pickle
        # file, or any other formats. The only thing you need to gua-
        # rantee is the `self.path_list` must be given a valid value. 
        file_list_path = os.path.join(self.data_dir, 'file_list.pkl')
        with open(file_list_path, 'rb') as f:
            file_list = pkl.load(f)

        fl_train, fl_val = train_test_split(
            file_list, test_size=0.2, random_state=2333)
        self.path_list = fl_train if self.train else fl_val

        label_file = './data/ref/label_dict.pkl'
        with open(label_file, 'rb') as f:
            self.label_dict = pkl.load(f)

    def __len__(self):
        return len(self.path_list)

    def __getitem__(self, idx):
        path = self.path_list[idx]
        filename = op.splitext(op.basename(path))[0]
        img = np.load(path).transpose(1, 2, 0)

        labels = self.to_one_hot(self.label_dict[filename.split('_')[0]])
        labels = torch.from_numpy(labels).float()

        trans = torch.nn.Sequential(
            transforms.RandomHorizontalFlip(self.aug_prob),
            transforms.RandomVerticalFlip(self.aug_prob),
            transforms.RandomRotation(10),
            transforms.RandomCrop(128),
            transforms.Normalize(self.img_mean, self.img_std)
        ) if self.train else torch.nn.Sequential(
            transforms.CenterCrop(128),
            transforms.Normalize(self.img_mean, self.img_std)
        )

        img_tensor = trans(img)

        return img_tensor, labels, filename