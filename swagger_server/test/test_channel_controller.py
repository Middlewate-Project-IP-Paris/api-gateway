# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChannelController(BaseTestCase):
    """ChannelController integration test stubs"""

    def test_api_v1_channel_idids_get(self):
        """Test case for api_v1_channel_idids_get

        Get Channels by ID
        """
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/channel/id={ids}'.format(ids=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_channel_join_invite_link_get(self):
        """Test case for api_v1_channel_join_invite_link_get

        Join channel by link
        """
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/channel/join/{invite_link}'.format(invite_link='invite_link_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
