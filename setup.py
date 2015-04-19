
from setuptools import setup, find_packages

import pyslate

from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), 'rt') as f:
    long_description = f.read()


setup(
    name='pyslate',
    version=pyslate.__version__,
    description='A translation library.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: MIT License",
    ],
    author=pyslate.__author__,
    author_email='grkalk@gmail.com',
    maintainer=pyslate.__author__,
    maintainer_email='grkalk@gmail.com',
    url='https://github.com/GreeKpl/pyslate',
    license='MIT',
    test_suite='tests',
    packages=find_packages(),
    install_requires=[
        'ply>=3.4',
    ],
)
