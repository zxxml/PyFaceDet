#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import setuptools

# the name PyFace is used
# use PyFaceDet instead :P
setuptools.setup(
    name='PyFaceDet',
    version='0.2.0',
    author='zxxml',
    author_email='zxxml@outlook.com',
    url='https://github.com/zxxml/PyFace',
    description='See GitHub for details.',
    packages=setuptools.find_packages(),
    package_data={'': ['*.dll', '*.so']},
    install_requires=['numpy', 'Pillow']
)
