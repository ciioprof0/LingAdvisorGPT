#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/adapters/generic_repo.py

""" Adapter module for the repository. """

from src.adapters.repository import AbstractRepository
from src.domain import model


class GenericRepository(AbstractRepository):
    """Generic repository class for adding and getting items."""

    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()

    def modify(self, reference, eta, sku, qty):
        batch = self.get(reference)
        batch._eta = eta
        batch._sku = sku
        batch._qty = qty
        return batch

    def save(self, batch):
        self.session.add(batch)
        return batch