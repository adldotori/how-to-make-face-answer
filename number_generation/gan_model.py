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
class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Sequential(
            torch.nn.Linear(100, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 784))
        self.layer.apply(weights_init)

    def forward(self, x):
        return self.layer(x)
        
class Discriminator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Sequential(
            torch.nn.Linear(784, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, 1))
        self.layer.apply(weights_init)

    def forward(self, x):
        return self.layer(x)

# initialize
generator = Generator()
discriminator = Discriminator()

for images, labels in train_loader:
    images = images.view(-1, 784)
    z = torch.randn(batch_size, 100) # define latent vector.

    # forward
    fake_images = generator(z)
    valid = discriminator(fake_images)
    print(fake_images.shape)
    print(valid.shape)
    exit()

'''
torch.Size([100, 784])
torch.Size([100, 1])
'''