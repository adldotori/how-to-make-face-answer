import torch

torch.manual_seed(17)

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

    def print_parameter(self):
        print(f'a = {self.linear.weight}, b = {self.linear.bias}\n')
        
# data
x_data = torch.tensor([[1.0], [2.0], [3.0]]) # shape : (3, 1)
y_data = torch.tensor([[1.0], [3.0], [5.0]])

# initialize
model = Model() # Model.__init__()
optim = torch.optim.SGD(model.parameters(), lr=0.1)
criterion = torch.nn.MSELoss()
model.print_parameter()

for epoch in range(100):
    # forward
    predict = model(x_data) # == model.forward(x_data)

    # compute loss
    loss = criterion(predict, y_data) # shape : (3) -> ()

    # backward
    loss.backward()
    optim.step()
    optim.zero_grad()

    if not (epoch+1) % 10:
        print(f'Epoch : {epoch+1}')
        print(f'Predict : {predict}')
        print(f'Loss = {loss}')
        model.print_parameter()
        
'''
Epoch : 100
Predict : tensor([[1.0847],
        [3.0182],
        [4.9516]], grad_fn=<AddmmBackward>)
Loss = 0.003282001242041588
a = Parameter containing:
tensor([[1.9351]], requires_grad=True), b = Parameter containing:
tensor([-0.8524], requires_grad=True)
'''