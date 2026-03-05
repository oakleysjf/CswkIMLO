import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision.datasets import OxfordIIITPet
import torchvision.transforms as transforms

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
    print("## SUPERVISED LEARNING ##\n Breed Classifier\n")

    pass

class CNN(nn.Module):

    def __init__(self, num_classes: int = 37):
        super().__init__()
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        pass

# -- Data Loading and Transforms --
def load_dataset(data_dir: str, 
                 split: str = 'trainval') -> Dataset:
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
    main()
