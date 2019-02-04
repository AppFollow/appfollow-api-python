import unittest
from unittest.mock import Mock

from requests import Response

from appfollow_api import ApiError, AppFollowAPI


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = AppFollowAPI('cid', 'secret')

    def test_make_sign(self):
        sign = self.api._make_sign('/path', {'type': '1'})
        expected_sign = '795bedc6f005459083627e77c12ed85a'
        self.assertEqual(sign, expected_sign)

    def test_api_error(self):
        response = Response()
        response.status_code = 200
        response.json = Mock(return_value={'error': {'msg': 'test error', 'code': 1}})
        self.api.session.get = Mock(return_value=response)
        with self.assertRaises(ApiError):
            self.api.collections()
