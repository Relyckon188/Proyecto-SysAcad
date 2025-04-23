import unittest
import os
from flask import current_app
from app import create_app
from app.models import 


class AutoridadTestCase(unittest.TestCase):
    def test_autoridad_creation(self):
        autoridad = Autoridad()
        
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'text'
        self.app = create_app()
        self.app_context = self.app.app_context
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
    
    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Dedicacion simple"
        cargo.nombre = "Decano"
        cargo.puntos = 100
        cargo.categoria_cargo = CategoriaCargo()
        cargo.categoria_cargo
        cargo.tipo_dedicacion
        autoridad.nombre = "Juan Perez"
        autoridad.cargo = cargo
        autoridad.telefono = "123456789"
        autoridad.email = "abc@gmail.com"
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertIsNotNone(autoridad.carga.categoría_ca)
        self.assertEqual(autoridad.cargo.categoría)
        
        