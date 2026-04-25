import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from torchvision.datasets import OxfordIIITPet
import torchvision.transforms as transforms
import sklearn.datasets

# -- Primary Model & Main Function --
def main(data_dir: str,
        batch_size: int,
        epochs: int, 
        learning_rate: float, 
        image_size: int,
        num_workers: int, save_path: str) -> None:
    """
    Main function to run epochs and training.

    Args:
        data_dir (str): directory of the data stored.
        batch_size (int): size of the input.
        epochs (int): number of epochs (Max 20!)
        learning_rate (float): rate at which the model learns.
        image_size (int): size of image, (intxint).
        num_workers (int): number of threads (may not be implemented.)
        save_path (str): path to save the training data.
    """

    pass

class CNN(nn.Module):

    def __init__(self,
                 input_features: list,
                 hidden_layers: list,
                 output_features: list,
                 activation_function: F.relu):
        super().__init__()
        if len(hidden_layers) < 1:
            raise ValueError()
        
        self.layers = []
        self.layers.append(nn.Linear(input_features, hidden_layers[0]))
        self.add_module("Input Layer", self.layers[0])

        for i in range(len(hidden_layers)):
            self.layers.append(nn.Linear(hidden_layers[i-1], hidden_layers[i]))
            self.add_module([f"Hidden Layer {i}"], self.layers[i])
        
        self.out = nn.Linear(hidden_layers[-1], output_features)
        self.add_module("Output Layer", self.out)

        self.activation_function = activation_function

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        for i in range(len(self.layers)):
            x = self.activation_function(self.layers[i](x))
        x = self.out
        return x

# -- Data Loading and Transforms --
def load_dataset(data_dir: str, 
                 split: str = 'trainval') -> Dataset:
    oxfordIIIpet = Dataset()
    oxfordIIIpet.__getitem__('')
    pass

def create_transforms(image_size: int) -> tuple[transforms.Compose, transforms.Compose]:
    pass

def create_dataloaders(
        train_dataset: Dataset,
        val_dataset: Dataset,
        batch_size: int,
        num_workers: int
) -> tuple[DataLoader, DataLoader]:
    pass

# -- Training Configuration -- 
def define_training(
        model: nn.Module,
        learning_rate: float,
) -> tuple[nn.Module, optim.Optimizer]:
    pass

def train():
    pass

# -- Validation and Saving Progress --

def save():
    pass

def validate():
    pass


if __name__ == '__main__':
    pass
