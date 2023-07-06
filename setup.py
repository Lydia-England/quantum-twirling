from setuptools import find_packages, setup
from quantum_twirling import __version__

setup(
    name='quantum_twirling',
    version=__version__,
    description='Sets of Pauli Twirls, generating function for Twirls',
    url='https://github.com/Lydia-England/quantum-twirling',
    author='Lydia England',
    author_email='lydiajoyengland@gmail.com',
    packages=find_packages(),
)
