# data
x_data = [1.0, 2.0, 3.0]
y_data = [1.0, 3.0, 5.0]

# initialize
a, b = 0, 0 
lr = 0.1

for epoch in range(100):
    loss = 0
    gradient_a = 0
    gradient_b = 0
    print(f'Epoch : {epoch+1}')
    print('Predict : ', end='')
    for x_val, y_val in zip(x_data, y_data):
        # forward
        predict = a * x_val + b
        print(f'{predict}',end=' ')

        # compute loss
        loss += (predict - y_val) ** 2 / len(x_data)

        # compute gradient
        gradient_a += 2 * x_val * (predict - y_val) / len(x_data)
        gradient_b += 2 * (predict - y_val) / len(x_data)

    print(f'\nLoss = {loss}')

    # backward
    a -= lr * gradient_a
    b -= lr * gradient_b
    print(f'a = {a}, b = {b}\n')
    
'''
Epoch : 100
Predict : 1.0793139169811063 3.0170206923315392 4.9547274676819715 
Loss = 0.002876667858939229
a = 1.939204261704426, b = -0.8617969968356342
'''