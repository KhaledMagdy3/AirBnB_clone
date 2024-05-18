#!/usr/bin/python3
"""TestBaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.base.to_dict()
        expected_dic = self.base.__dict__.copy()
        expected_dic["__class__"] = self.base.__class__.__name__
        expected_dic["updated_at"] = self.base.updated_at.isoformat()
        expected_dic["created_at"] = self.base.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.base.updated_at
        self.base.my_number = 90
        self.base.save()
        after_update_time = self.base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.base.__class__.__name__
        expected_str = f"[{n}] ({self.base.id}) <{self.base.__dict__}>"
        self.assertEqual(self.base.__str__(), expected_str)
