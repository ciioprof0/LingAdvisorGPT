#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests/random_refs.py

""" Random references for testing. """

import uuid


def random_suffix():
    """ Generate a random suffix. """
    return uuid.uuid4().hex[:6]


def random_ref1(name=""):
    """ Generate a random ref1. """
    return f"ref1-{name}-{random_suffix()}"


def random_ref2(name=""):
    """ Generate a random ref2. """
    return f"ref2-{name}-{random_suffix()}"


def random_ref3(name=""):
    """ Generate a random ref3. """
    return f"ref3-{name}-{random_suffix()}"