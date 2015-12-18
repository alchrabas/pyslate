
from setuptools import setup, find_packages

import pyslate

from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), 'rt') as f:
    long_description = f.read()


setup(
    name='pyslate',
    version=pyslate.__version__,
    description='A Python library for maintaining grammatically correct i18n (internationalization) of texts used in'
                'the program: translation of messages, formatting dates and numbers to provide multi-language support.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
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
        'six>=1.10',
    ],
)
