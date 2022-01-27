# Pytorch-Template
basic Pytorch-Template, got idea from https://github.com/miracleyoo/pytorch-lightning-template

# File Structure

```
root-
    |-data
        |-__init__.py
        |-abstract_dataloader.py
        |-abstract_dataset.py
        |-xxxdataset
            |-__init__.py
            |-xxx_dataloader.py
            |-xxx_dataset.py
            |-xxx_raw_data
                |-raw_data1.csv/json/pickle
                |-...
    |-model
        |-__init__.py
        |-abstract_model.py
        |-xxxmodel1.py
        |-xxxmodel2.py
        |-...
    |-trainer
        |-__init_-.py
        |-abstract_trainier.py
    |-main.py
    |-utils.py
```
