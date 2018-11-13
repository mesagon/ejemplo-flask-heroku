#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:07:18 2018

@author: jesus
"""

from flask import Flask
from flask import jsonify

# Crear la aplicacion.
app = Flask(__name__)

@app.route("/")
def hello_world():

        return(jsonify({"key":"Hello World!"}))

if __name__ == "__main__":
    
    # Lanzar aplicacion.
    app.run()
    
    
