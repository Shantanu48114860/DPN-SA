"""
MIT License

Copyright (c) 2020 Shantanu Ghosh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import torch
import torch.nn as nn
import torch.utils.data


class shallow_net(nn.Module):
    def __init__(self, training_mode, device):
        print("Training mode: {0}".format(training_mode))
        super(shallow_net, self).__init__()
        self.training_mode = training_mode

        # encoder
        self.encoder = nn.Sequential(nn.Linear(in_features=25, out_features=1),
                                     nn.Tanh()
                                     )

        if self.training_mode == "train":
            # decoder
            self.decoder = nn.Sequential(nn.Linear(in_features=1, out_features=25),
                                         nn.Tanh(),
                                         nn.Linear(in_features=25, out_features=25))

    def forward(self, x):
        if torch.cuda.is_available():
            x = x.float().cuda()
        else:
            x = x.float()

        # encoding
        x = self.encoder(x)

        if self.training_mode == "train":
            # decoding
            x = self.decoder(x)
        return x
