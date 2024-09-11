#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/service_layer/unit_of_work.py

"""Unit of Work (UoW) pattern for managing transactions."""

import abc

class AbstractUnitOfWork(abc.ABC):
    """Abstract UoW context manager"""
    def __exit__(self, *args):
        """Exit the UoW context manager."""
        self._commit()

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def _rollback(self):
        raise NotImplementedError

