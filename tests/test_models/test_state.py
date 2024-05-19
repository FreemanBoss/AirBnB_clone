#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Docs for test state"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        state = State()
        state.name = "Lagos"
        self.assertIsNotNone(state.updated_at)
        self.assertIsNotNone(state.id)
        self.assertEqual(state.name, "Lagos")


if __name__ == "__main__":
    unittest.main()
