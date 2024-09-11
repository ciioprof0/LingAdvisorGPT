#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/setup.py

""" This module makes the package installable with `pip`. """

from setuptools import setup, find_packages

# Minimal setup.py file
setup(
    name='your_package_name',
    version='0.1',
    packages=['your_pkg_name'],
    # Automatically find packages, exclude tests
    # packages=find_packages(exclude=['tests*', 'migrations']),
)

# Full setup.py file
# setup(
#     name='display_name',  # Name of your package
#     version='0.1.0',  # Semantic versioning: major.minor.patch
#     # Detailed description from README
#     description='A short description of your package',
#     long_description=open('README.md', encoding='utf-8').read(),
#     long_description_content_type='text/markdown',  # Content type for long description
#     author='Your Name',
#     author_email='your.email@example.com',
#     url='https://github.com/yourusername/yourproject',  # URL to the project's homepage
#      # Automatically find packages, exclude tests
#     packages=find_packages(exclude=['tests*', 'migrations']),
#     include_package_data=True,  # Include non-Python files listed in MANIFEST.in
#     install_requires=[
#         'dependency1>=1.0.0,<2.0.0',
#         'dependency2>=2.0.0,<3.0.0',
#     ],  # External packages required by your project
#     extras_require={
#         'dev': [
#             'pytest>=6.0.0,<7.0.0',
#             'flake8>=3.8.0,<4.0.0',
#             'mypy>=0.800,<1.0.0'
#         ],
#     },  # Additional dependencies for development
#     entry_points={
#         'console_scripts': [
#             'command_name=module:function_name',
#         ],
#     },  # CLI commands
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],  # Optional classifiers that provide metadata
#     python_requires='>=3.6',  # Python version compatibility
# )
