from prediction_model.config import config

with open(config.PACKAGE_ROOT/"VERSION") as f:
    __version__ = f.read().strip()

print(f'Model ver {__version__}')
