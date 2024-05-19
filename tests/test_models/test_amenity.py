#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Docs for test amenity"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        amenity = Amenity()
        amenity.name = "Laptop"
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "Laptop")


if __name__ == "__main__":
    unittest.main()
