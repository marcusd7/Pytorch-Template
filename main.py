import os
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    # Basic Training Control
    parser.add_argument('--batch_size', default=32, type=int)
    parser.add_argument('--num_workers', default=8, type=int)
    parser.add_argument('--seed', default=1234, type=int)
    parser.add_argument('--lr', default=1e-3, type=float)

    # LR Scheduler
    parser.add_argument('--lr_scheduler', choices=['step', 'cosine'], type=str)
    parser.add_argument('--lr_decay_steps', default=20, type=int)
    parser.add_argument('--lr_decay_rate', default=0.5, type=float)
    parser.add_argument('--lr_decay_min_lr', default=1e-5, type=float)

    # Restart Control
    parser.add_argument('--load_best', action='store_true')
    parser.add_argument('--load_dir', default=None, type=str)
    parser.add_argument('--load_ver', default=None, type=str)
    parser.add_argument('--load_v_num', default=None, type=int)

    # Training Info
    parser.add_argument('--dataset', default='standard_data', type=str)
    parser.add_argument('--data_dir', default='ref/data', type=str)
    parser.add_argument('--model_name', default='standard_net', type=str)
    parser.add_argument('--loss', default='bce', type=str)
    parser.add_argument('--weight_decay', default=1e-5, type=float)
    parser.add_argument('--no_augment', action='store_true')
    parser.add_argument('--log_dir', default='lightning_logs', type=str)
    
    # Model Hyperparameters
    parser.add_argument('--hid', default=64, type=int)
    parser.add_argument('--block_num', default=8, type=int)
    parser.add_argument('--in_channel', default=3, type=int)
    parser.add_argument('--layer_num', default=5, type=int)

    # Other
    parser.add_argument('--aug_prob', default=0.5, type=float)

    # Reset Some Default Trainer Arguments' Default Values
    parser.set_defaults(max_epochs=100)

    args = parser.parse_args()