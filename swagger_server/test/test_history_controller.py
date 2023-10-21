# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHistoryController(BaseTestCase):
    """HistoryController integration test stubs"""

    def test_api_v1_history_history_data_channel_idchannel_id_post_idspost_id_get(self):
        """Test case for api_v1_history_history_data_channel_idchannel_id_post_idspost_id_get

        Get Channels history by ID
        """
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/history/{history_data}/channel_id={channel_id}/post_ids={post_id}'.format(channel_id=56, post_id=56, history_data='history_data_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_history_history_data_idids_get(self):
        """Test case for api_v1_history_history_data_idids_get

        Get Channels history by ID
        """
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/history/{history_data}/id={ids}'.format(ids=56, history_data='history_data_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
