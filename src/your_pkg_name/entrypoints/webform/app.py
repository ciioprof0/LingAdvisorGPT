#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/entrypoints/webform/app.py

""" Entry point for the Flask application. """

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission here
        return "Form submitted!"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
