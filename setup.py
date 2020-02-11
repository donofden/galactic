# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Galactic',
    version='1.0.0',
    description='Galactic is project which binds software with outer space, its a fun project to understand outspace and python :) ',
    long_description=readme,
    author='DonOfDen',
    author_email='me@donofden.com',
    url='https://github.com/donofden/galactic',
    license=license,
    packages=find_packages(exclude=('docs'))
)