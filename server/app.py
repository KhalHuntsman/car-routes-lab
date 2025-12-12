#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Minimal Flask application for the Flatiron Cars lab.

The app provides:
- A home route ("/") that displays a welcome message
- A dynamic route ("/<model>") that checks for valid car models
"""

from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# List of available car models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route("/")
def index():
    """Display a welcome message on the home page."""
    return "Welcome to Flatiron Cars"


@app.route("/<string:model>")
def model(model):
    """Display model information if it exists in the catalog."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"
