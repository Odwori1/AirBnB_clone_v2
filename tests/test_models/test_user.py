#!/usr/bin/python3
""" Unittests for User class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Defines tests for the User class"""

    def __init__(self, *args, **kwargs):
        """ Constructor, Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test the data type of the 'first_name' attribute in the User class"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test the data type of the 'last_name' attribute in the User class"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test the data type of the 'email' attribute in the User class"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test the data type of the 'password' attribute in the User class"""
        new = self.value()
        self.assertEqual(type(new.password), str)
