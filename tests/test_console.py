#!/usr/bin/python3
"""unnitest for the console.py file"""
import unittest
import console


class TestHBNBCommandPrompt(unittest.TestCase):
    """unittesting the prompt of the project interpreter"""
    def test_prompt(self):
        self.assertTrue(console.HBNBCommand.prompt, "(hbnb) ")
