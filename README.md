# Pytorch-Template
Pytorch-Template

# File Structure
refer to https://github.com/miracleyoo/pytorch-lightning-template


```
root-
	|-data
		|-__init__.py
		|-abstract_data_interface.py
		|-abstract_dataset.py
        |-xxxdataset
            |-__init__.py
            |-xxx_data_interface.py
            |-xxx_dataset.py
            |-xxx_raw_data
                |-raw_data1.csv/json/pickle
                |-...
	|-model
		|-__init__.py
		|-model_interface.py
		|-xxxmodel1.py
		|-xxxmodel2.py
		|-...
    |-trainer
        |-__init_-.py
	|-main.py
	|-utils.py
```
