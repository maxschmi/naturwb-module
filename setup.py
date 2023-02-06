from setuptools import setup, find_packages
from naturwb import naturwb

def readme():
    with open('README.md') as f:
        return f.read()

def requirements():
    with open('requirements.txt') as f:
        return f.readlines()

setup(
   name='NatUrWB',
   version=naturwb.__version__,
   description='This is a package to calculate the NatUrWB reference from the database.',
   long_description=readme(),
   classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Hydrology',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Intended Audience :: Science/Research',
        'Natural Language :: English'
      ],
   author='Max Schmit',
   author_email='max.schmit@hydrology.uni-freiburg.de',
   url='https://github.com/maxschmi/naturwb-module',
   license='GNU GPT3',
   packages=find_packages(include=['naturwb', 'naturwb.*']), 
   install_requires=requirements(),
   python_requires='>=3.6, <4',
)