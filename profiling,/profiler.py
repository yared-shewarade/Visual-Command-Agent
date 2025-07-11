import torch
import torch.profiler 
from training.model import VisualCommandModel 
from training.dataset import DummyVLCommandDataset 
from torch.utils.data import DataLoader 

NUM_CLASSES = 5 
BATCH_SIZE = 4 
DEVICE = torch.device("cude" if torch.cuda.is_available() else "cpu")

model = VisualCommandModel(num_classes=NUM_CLASSES).to(DEVICE)
model.train() 
loader = DataLoader(DummyVLCommandDataset(num_samples=20), batch_size=BATCH_SIZE)
optimizer = torch.optim.Adam(model.parameters())
loss_fn = torch.nn.CrossEntropyLoss() 

with torch.profiler.profile(
    schedule=torch.profiler.schedule(wait=1, warmup=1, active=3),
    on_trace_ready=torch.profiler.tensorboard_trace_handler("./logs/profiler"),
    record_shapes=True,
    with_stack=True
) as prof:
    for step, (images, texts, labels) in enumerate(loader):
        if step >= 6:
            break
        images, texts, labels = images.to(DEVICE), texts.to(DEVICE), labels.to(DEVICE)
        optimizer.zero_grad() 
        outputs = model(images, texts)
        loss = loss_fn(outputs, labels)
        loss.backward() 
        optimizer.step()
        print.step() 
print("Profiling complete. Run 'tensorboard --logdir=./logs/profiler' to view results.")
