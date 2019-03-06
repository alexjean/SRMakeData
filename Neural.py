# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 下午 04:10
# @Author  : AlexJean
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init

class Net(nn.Module):

    LearningRate = 0.0001

    def __init__(self):
        super(Net, self).__init__()
        # Conv2d input形式為(batchN,C_in,H,W)
        # outout 為(batchN,C_out,H,W)
        self.conv1 = nn.Conv2d(1, 64, (5, 5), stride=(1, 1), padding=(2, 2))
        self.conv2 = nn.Conv2d(64, 64, (3, 3), (1, 1), (1, 1))
        self.conv3 = nn.Conv2d(64, 64, (3, 3), (1, 1), (1, 1))
        self.conv4 = nn.Conv2d(64,  4, (3, 3), (1, 1), (1, 1))
        self._initialize_weights()

    def forward(self, x):
        x = F.tanh(self.conv1(x))
        x = F.tanh(self.conv2(x))
        x = F.tanh(self.conv3(x))
        x = F.sigmoid(self.conv4(x))           # [batch, 5, H, W]
        return x

    def _initialize_weights(self):
        init.xavier_normal(self.conv1.weight, init.calculate_gain('tanh'))
        init.xavier_normal(self.conv2.weight, init.calculate_gain('tanh'))
        init.xavier_normal(self.conv3.weight, init.calculate_gain('tanh'))
        init.orthogonal_(self.conv4.weight, init.calculate_gain('sigmoid'))
