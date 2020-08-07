import torch
import torchvision
import torchvision.transforms as transforms

torch.manual_seed(17) # eliminate random.

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

for images, labels in train_loader:
    print(images.shape) # torch.Size([100, 1, 28, 28])
    images = images.view(-1, 784)
    print(images.shape) # torch.Size([100, 784])

    # forward
    predict = model(images)
    print(predict.shape)
    exit()
    
'''
torch.Size([100, 1, 28, 28])
torch.Size([100, 784])
torch.Size([100, 10])
'''