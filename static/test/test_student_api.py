# coding: utf-8

"""
    Lab 2 API made with love by Roman Kovalchuk

    variant №12  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.student_api import StudentApi  # noqa: E501
from openapi_client.rest import ApiException


class TestStudentApi(unittest.TestCase):
    """StudentApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.student_api.StudentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_student_id_get(self):
        """Test case for student_id_get

        """
        pass

    def test_student_id_post(self):
        """Test case for student_id_post

        New Student.  # noqa: E501
        """
        pass

    def test_student_id_put(self):
        """Test case for student_id_put

        Update student.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()