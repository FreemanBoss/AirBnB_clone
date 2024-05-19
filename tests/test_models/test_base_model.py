#!/usr/bin/python3
"""Documenting the user model"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """The test class for basemodel."""

    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.model1.name = "Model 1"
        self.model1.num = 1
        self.model2.name = "Model 2"
        self.model2.num = 2

    def tearDown(self):
        del self.model1
        del self.model2

    def test_id(self):
        self.assertIsNotNone(self.model1.id)
        self.assertIsInstance(self.model1.id, str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_dateimes(self):
        now = datetime.now()
        self.assertIsInstance(self.model1.created_at, datetime)
        self.assertIsInstance(self.model1.updated_at, datetime)
        self.assertIsInstance(self.model2.created_at, datetime)
        self.assertIsInstance(self.model2.updated_at, datetime)
        self.assertLessEqual(self.model1.created_at, now)
        self.assertLessEqual(self.model1.updated_at, now)

    def test_str(self):
        str_gotten = str(self.model1)
        str_expected = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        self.assertEqual(str_gotten, str_expected)

    def test_save(self):
        prev = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(prev, self.model1.updated_at)
        self.assertLessEqual(self.model1.created_at, self.model1.updated_at)

    def test_todict(self):
        obj_dict = self.model1.to_dict()
        self.assertIsNotNone(obj_dict["created_at"])
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["id"], str)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], self.model1.id)


if __name__ == "__main__":
    unittest.main()
