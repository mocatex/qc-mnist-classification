"""
Download MNIST dataset and save it to folder-structured format:

mnist_data/
    train/
    val/
    test/
"""

import shutil
from pathlib import Path
from torchvision import datasets
from torch.utils.data import random_split

DATA_ROOT = Path(__file__).parent.parent / "mnist_data"
TRAIN_DIR = DATA_ROOT / "train"
VAL_DIR = DATA_ROOT / "val"
TEST_DIR = DATA_ROOT / "test"
VAL_SPLIT = 0.1

for d in [TRAIN_DIR, VAL_DIR, TEST_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Download MNIST using torchvision
train_dataset = datasets.MNIST(root="../mnist_data", train=True, download=True)
test_dataset = datasets.MNIST(root="../mnist_data", train=False, download=True)

# Split train -> train + val
val_size = int(VAL_SPLIT * len(train_dataset))
train_size = len(train_dataset) - val_size
train_ds, val_ds = random_split(train_dataset, [train_size, val_size])


def save_dataset(dataset, folder: Path):
    for idx, (img_tensor, label) in enumerate(dataset):
        img = img_tensor
        img.save(folder / f"img-{idx}_label-{label}.png")


print("Saving training images...")
save_dataset(train_ds, TRAIN_DIR)
print(f"Saved {len(train_ds)} images to {TRAIN_DIR}\n")

print("Saving validation images...")
save_dataset(val_ds, VAL_DIR)
print(f"Saved {len(val_ds)} images to {VAL_DIR}\n")

print("Saving test images...")
save_dataset(test_dataset, TEST_DIR)
print(f"Saved {len(test_dataset)} images to {TEST_DIR}\n")

# clean MNIST folder
shutil.rmtree("../mnist_data/MNIST")
print("Cleaned up MNIST folder.\n")

print("Done!")
