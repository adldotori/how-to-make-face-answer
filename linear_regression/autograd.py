import torch

# data
x_data = torch.tensor([1.0, 2.0, 3.0])
y_data = torch.tensor([1.0, 3.0, 5.0])

# initialize
a, b = torch.tensor([0.0], requires_grad=True), torch.tensor([0.0], requires_grad=True)
lr = 0.1

def forward(x_data):
    return a * x_data + b

def get_loss(predict, y_data):
    return torch.sum((predict - y_data) ** 2) / len(y_data)

for epoch in range(100):
    # forward
    predict = forward(x_data) # shape : (3)

    # compute loss
    loss = get_loss(predict, y_data) # shape : (3) -> ()

    # backward
    loss.backward()
    a.data = a.data - lr * a.grad # shape : (1)
    b.data = b.data - lr * b.grad # shape : (1)
    a.grad.zero_()
    b.grad.zero_()

    if not (epoch+1) % 10:
        print(f'Epoch : {epoch+1}')
        print(f'Predict : {predict}')
        print(f'Loss = {loss}')
        print(f'a = {a}, b = {b}\n')
        
'''
Epoch : 100
Predict : tensor([1.0793, 3.0170, 4.9547], grad_fn=<AddBackward0>)
Loss = 0.00287666660733521
a = tensor([1.9392], requires_grad=True), b = tensor([-0.8618], requires_grad=True)
'''