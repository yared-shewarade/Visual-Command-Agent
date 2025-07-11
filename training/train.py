import torch
import torch.nn as nn     
import torch.optim as optim 
from torch.utils.data import DataLoader  
from model import VisualCommandModel 
from dataset import DummyVLCommandDataset 

NUM_CLASSES = 5
BATCH_SIZE = 4 
EPOCHS = 3
DEVICE = torch.device("cude" if torch.cuda.is_available() else "cpu")

model = VisualCommandModel(num_classes=NUM_CLASSES).to(DEVICE)
criterion = nn.CrossEntropyLoss() 
optimizer = optim.Adam(model.parameters(), lr=le - 4)

train_dataset = DummyVLCommandDataset(num_samples=100)
train_loader = DataLoader(train_dataset, batch - size=BATCH_SIZE, shuffle=True)
