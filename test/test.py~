#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:00:12 2018

@author: jesus
"""

import unittest
from flask import Flask
from flask import jsonify
import os,sys,inspect

# Importar el modulo de la aplicacion.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from .. import app

class testApp(unittest.TestCase):
    
    # Activamos bandera de test y creamos el cliente
    # de test.
    def setUp(self):
        
        app.app.testing = True
        self.app = app.app.test_client()
        

    # Testeamos la ruta /.
    def testRoot(self):
        
        with app.app.app_context():
            
            result = self.app.get("/")
            self.assertEqual(result.mimetype,"application/json")
            self.assertEqual(result.status,"200 OK")
            self.assertEqual(result.data,b'{"key":"Hello World!"}\n')
            
if __name__ == "__main__":

    unittest.main()        
        
        