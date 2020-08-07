import torch

# data
x_data = torch.tensor([1.0, 2.0, 3.0])
y_data = torch.tensor([1.0, 3.0, 5.0])

# initialize
a, b = torch.tensor([0.0]), torch.tensor([0.0])
lr = 0.1

for epoch in range(100):
    # forward
    predict = a * x_data + b # shape : (3)

    # compute loss
    loss = torch.sum((predict - y_data) ** 2) / len(x_data) # shape : (3) -> ()

    # backward
    gradient_a = 2 * torch.sum(x_data * (predict - y_data)) / len(x_data) # shape : (3) -> ()
    gradient_b = 2 * torch.sum((predict - y_data)) / len(x_data) # shape : (3) -> ()

    a -= lr * gradient_a # shape : (1)
    b -= lr * gradient_b # shape : (1)

    if not (epoch+1) % 10:
        print(f'Epoch : {epoch+1}')
        print(f'Predict : {predict}')
        print(f'Loss = {loss}')
        print(f'a = {a}, b = {b}\n')

'''
Epoch : 100
Predict : tensor([1.0793, 3.0170, 4.9547])
Loss = 0.00287666660733521
a = tensor([1.9392]), b = tensor([-0.8618])
'''