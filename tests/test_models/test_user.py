#!/usr/bin/python3
"""Unittest for User model"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")


if __name__ == '__main__':
    unittest.main()
