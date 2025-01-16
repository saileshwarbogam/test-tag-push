
from setuptools import setup, find_packages
import sys


if sys.version_info < (3, 8):
    raise RuntimeError("requires Python 3.8+")
current_version = '2.0.0b51'

setup(
    name='hellosaib',
    version=current_version,
    author='Sailesh',
    author_email='test@gmail.com',
    packages=find_packages(where='.', exclude=['test*']),
    license='LICENSE',
    description=' Python programming language',
    long_description=open('README.rst').read(),
    install_requires=[
],
    python_requires=">=3.8"
)
