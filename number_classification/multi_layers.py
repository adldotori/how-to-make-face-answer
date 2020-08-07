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


def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Linear') != -1:
        torch.nn.init.kaiming_uniform_(m.weight)

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Sequential(
            torch.nn.Linear(784, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, 10))
        self.layer.apply(weights_init)

    def forward(self, x):
        return self.layer(x)

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

# test
with torch.no_grad():
    total = 0
    correct = 0
    for images, labels in test_loader:
        images = images.view(-1, 784)

        # forward
        predict = model(images)
        _, predict = torch.max(predict.data, 1)
        total += labels.size(0)
        correct += (predict == labels).sum()
    print('Accuracy : {}%'.format(correct * 100 // total))
    
'''
Epoch : 20
Loss = 0.0017913138726726174

Accuracy : 98%
'''