#!/usr/bin/env python
# -*- coding: utf-8 -*-
#src/your_pkg_name/config.py

"""This module contains the configuration variables for the application."""

import os


class Config:
    """Set Flask configuration vars from .env file."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecret')
