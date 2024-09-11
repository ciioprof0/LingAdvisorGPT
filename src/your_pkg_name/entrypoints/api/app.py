#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/entrypoints/api/app.py

""" Entry point for the Flask application. """

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_home():
    """API home route."""
    return jsonify({"message": "Hello, HexArch!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
