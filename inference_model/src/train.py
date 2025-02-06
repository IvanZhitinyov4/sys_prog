import torch
import torch.nn as nn

from data_prep import create_sequences


class Model(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(self).__init__()
        self.hidden_size = hidden_size
        self.input_size = input_size
        self.output_size = output_size
        self.num_layers = num_layers
        self.fc = nn.Linear(hidden_size, output_size)