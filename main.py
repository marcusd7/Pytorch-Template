from data import AbstractDataSet

dataset = AbstractDataSet(data_dir="data\\xxxdataset\\xxx_raw_data", file_list_type='csv')
print(len(dataset))
print(dataset[1])
print(dataset.test_list)
print(dataset.train_list)