import torch
import torch.nn as nn
from math import sqrt


class Asym_ReLU_Block(nn.Module):
    def __init__(self):
        super(Asym_ReLU_Block, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(
            3, 0), stride=1, padding=(1, 0), bias=False)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(
            0, 3), stride=1, padding=(0, 1), bias=False)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        return self.relu(self.conv2(self.conv1(x)))


class Asym_Net(nn.Module):
    def __init__(self):
        super(Asym_Net, self).__init__()
        self.residual_layer = self.make_layer(Asym_ReLU_Block, 18)
        self.input = nn.Conv2d(
            in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1, bias=False)
        self.output = nn.Conv2d(
            in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1, bias=False)
        self.relu = nn.ReLU(inplace=True)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, sqrt(2. / n))

    def make_layer(self, block, num_of_layer):
        layers = []
        for _ in range(num_of_layer):
            layers.append(block())
        return nn.Sequential(*layers)

    def forward(self, x):
        residual = x
        out = self.relu(self.input(x))
        out = self.residual_layer(out)
        out = self.output(out)
        out = torch.add(out, residual)
        return out
