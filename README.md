# ml_helpers
Python package of helper functions when exploring data, preparing a label file and analysing model performance.

## Installing the Package
1. Clone this repi by navigating to code, then copying the repo link
2. Navigate in your Python terminal to the folder you wish to copy the package in and execute the command `git clone <repo link from step 1>`
3. Activate virtual environment you wish to install package in `conda activate <venv>`
4. Install package with command `pip install .`
5. To quickly test if package was successfully installed, employ python in the terminal to import the package and function in package: `python` > `import ml_helpers` > `from ml_helpers.fns import weights` 
6. To uninstall the package execute the command `pip uninstall ml_helpers`

## Updating the Package
If you wish to update the package follow "Installing the Package" instructions but use `pip install -e .` in step 4. This will mean that as you update the functions you will be able to use the updated version in real time without needing to reinstall the package.

## Unit Tests
1. navigate to appropriate venv and folder in terminal
2. run tests by executing `python tests.py`
