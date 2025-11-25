# MNIST Classification - a Quantum Computing Approach

This is a Quantum Computing approach to MNIST digit classification using PyTorch, TorchVision, and PennyLane.
We investigate how quantum circuits can be beneficial in learning to classify MNIST digits.
For that we start with a classical approach and introduce quantum circuits step by step.

## Installation and Setup

### Packages

After you cloned the repo you can get started by installing the required packages.

We are using [uv](https://docs.astral.sh/uv/) as our package manager. <br />
You can find here a quick [guide](https://mocatex.github.io/mocatex-wiki/python/uv-package-manager/) to get started.

So you need uv [installed](https://docs.astral.sh/uv/getting-started/installation/) on your system. <br />

On the repo there is a file called [pyproject.toml](pyproject.toml) which contains all the dependencies needed for this project. <br />
Together with a [uv.lock](uv.lock) file which contains the exact versions of the packages.

To install all packages simply run:

```bash
uv sync
```

### Datasets

To download the MNIST dataset and prepare it into the correct folder structure, there is a [script](scripts/mnist_data_loader.py) included.
Simply run it, and all images will be downloaded and saved in the correct folder structure.




