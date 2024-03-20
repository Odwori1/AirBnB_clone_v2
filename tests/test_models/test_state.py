#!/usr/bin/python3
""" Unittests for State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Defines tests for the State class"""

    def __init__(self, *args, **kwargs):
        """ Constructor, Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test the data type of the 'name' attribute in the Place class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
