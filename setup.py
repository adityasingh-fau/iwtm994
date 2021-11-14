from distutils.core import setup
from setuptools import find_packages
setup(name='iwtm994',
version='0.2',
author='DSSS',
author_email='aditya.singh@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets', 'opencv-python'])
