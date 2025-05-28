#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_exists(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))

    def test_created_updated_at(self):
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_to_dict_contains_keys(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)


if __name__ == '__main__':
    unittest.main()
