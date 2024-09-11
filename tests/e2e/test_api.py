#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests/e2e/test_api.py

""" Unit tests for the API module. """

import pytest
from src.your_pkg_name.entrypoints.api.app import app

@pytest.fixture
def client():
    """Create a test client for the API."""
    with app.test_client() as client:
        yield client

def test_api_home(client):
    """Test the API home route"""
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, HexArch!"}
