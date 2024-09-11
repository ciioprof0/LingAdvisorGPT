#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/adapters/repository.py

"""
The repository interface is an abstract class that defines the methods that
must be implemented by any repository class.
"""

import abc

class AbstractRepository(abc.ABC):
    """Abstract base class for a repository with add and get methods."""

    @abc.abstractmethod
    def add(self, item):
        """Add an item to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, identifier):
        """Get an item from the repository by its identifier."""
        raise NotImplementedError

    # @abc.abstractmethod
    # def list(self):
    #     """List all items in the repository."""
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def modify(self, identifier, item):
    #     """Modify an item in the repository."""
    #     raise NotImplementedError
