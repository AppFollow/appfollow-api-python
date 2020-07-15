import unittest
from unittest.mock import Mock

from requests import Response

from appfollow_api import ApiError, AppFollowAPI


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = AppFollowAPI('cid', 'secret')

    def test_api_error(self):
        response = Response()
        response.status_code = 200
        response.json = Mock(return_value={'error': {'msg': 'test error', 'code': 1}})
        self.api.session.get = Mock(return_value=response)
        with self.assertRaises(ApiError):
            self.api.collections()
        response.json.assert_called_once()

    def test_network_error(self):
        response = Response()
        response.status_code = 504
        response.json = Mock()
        self.api.session.get = Mock(return_value=response)
        with self.assertRaises(ApiError):
            self.api.collections()
        response.json.assert_not_called()
