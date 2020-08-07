import torch
import torchvision
import torchvision.transforms as transforms

torch.manual_seed(17)

batch_size = 100

# MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='../../data', 
                                           train=True, 
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = torchvision.datasets.MNIST(root='../../data', 
                                          train=False, 
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                                          batch_size=batch_size, 
                                          shuffle=False)

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x):
        return self.linear(x)

# initialize
model = Model()
optim = torch.optim.SGD(model.parameters(), lr=0.1)
criterion = torch.nn.CrossEntropyLoss()

# train
for epoch in range(20):
    for images, labels in train_loader:
        images = images.view(-1, 784)

        # forward
        predict = model(images)
        
        # backward
        loss = criterion(predict, labels)
        loss.backward()
        optim.step()
        optim.zero_grad()
    
    print(f'Epoch : {epoch+1}')
    print(f'Loss = {loss}\n')
    
'''
Epoch : 20
Loss = 0.2772206962108612
'''