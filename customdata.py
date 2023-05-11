import torch
from torch_geometric.data import Dataset

class custom_data(Dataset):
    def __init__(self,transform=None,device='cpu'):
        