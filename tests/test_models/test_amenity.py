#!/usr/bin/python3
""" Unittests for Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Defines tests for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """ Constructor, Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test the data type of the 'name' attribute in Amenity class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
