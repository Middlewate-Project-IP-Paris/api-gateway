# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHistoryController(BaseTestCase):
    """HistoryController integration test stubs"""

    def test_api_v1_history_object_type_history_data_idids_get(self):
        """Test case for api_v1_history_object_type_history_data_idids_get

        Get Channels history by ID
        """
        response = self.client.open(
            '/Middleware/API-Gateway/1.0.0/api/v1/history/{object_type}/{history_data}/id={ids}'.format(ids=56, object_type='object_type_example', history_data='history_data_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
