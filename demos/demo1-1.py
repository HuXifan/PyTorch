# -*- coding: utf-8 -*-
import torch
from torch.autograd import Variable

# print(torch.cuda.is_available())  # True

tensor1 = torch.Tensor(3, 2)
# print(tensor1, type(tensor1))
# print(tensor1.size())  # torch.Size([3, 2])
# b = tensor1.numpy()
# print(b, type(b))

print('__' * 20)
x = Variable(torch.Tensor([3]), requires_grad=True)
y = Variable(torch.Tensor([5]), requires_grad=True)
z = 2 * x + y + 4
z.backward()
# print('dz/dx:{}'.format(x.grad.data)) # dz/dx:tensor([2.])
# print('dz/dy:{}'.format(y.grad.data))  # dz/dy:tensor([1.])
print(z)
