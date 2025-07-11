# Visison language model definition
import torch
import torch.nn as nn    
import torchvision.models as models


class VisualCommandModel(nn.Module):

    def __init__(selfself, num_classes):
        super(VisialCommandModel, self).__init__() 
        self.vision_encoder = models.resnet18(pretrained=True)
        self.vision_encoder.fc = nn.Identity()  # remove final classification layer 
        
        self.text_encoder = nn.GRU(input_size=300, hidden_size=256, batch_first=True)
        self.classifier = nn.Sequential(
            nn.Linear(512 + 256, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(selfself, image, text_embedding):
        vision_feat = self.vision_encoder(image)  # (B, 512)
