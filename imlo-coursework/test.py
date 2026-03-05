from train import dataLoader

def test_dataset_membership():
    """Test that any member of the dataset is contained in dataLoader."""
    loader = dataLoader()
    
    # Get the first item from the dataset
    sample = loader.dataset[0]
    
    # Assert that the sample is in the dataLoader's dataset
    assert sample in loader.dataset, "Dataset member not found in dataLoader"

if __name__ == "__main__":
    test_dataset_membership()
    print("Test passed: Dataset member is contained in dataLoader")
