# Dummy for Testing
import torch
from torch.utils.data import Dataset
import random 


class DummyCommandDataset(Dataset):

    def __init__(selfself, num_samples=100, num_classes=5, text_len=10):
        self.num_samples = num_samples 
        self.num_classes = num_classes
        self.text_len = text_len

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        image = torch.randn(3, 224, 224)
        text_embedding = torch.randn(self.text_len, 300)
        label = random.randint(0, self.num_classes - 1)
        return image, text_embedding, torch.tensor(label, dtype=torch.long)
