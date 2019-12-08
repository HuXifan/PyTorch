# -*- coding: utf-8 -*-
import torch
from torch import nn


class NetName(nn.Module):
    def __init__(self):
        super(NetName, self).__init__()
        # 可以添加各种网络层
        self.conv1 = nn.Conv2d(3, 10, 3)
        # 具体每种层的参数可以查看文档

    def forward(self, x):
        # 定义向前传播
        out = self.conv1(x)
        return out


'''这就是构建所有神经网络的模板，
不管构建卷积神经网络
还是循环神经网络
或者是生成对抗网络 都依赖于这个结构。'''
