# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostsController(BaseTestCase):
    """PostsController integration test stubs"""

    def test_api_v1_posts_channel_id_idids_get(self):
        """Test case for api_v1_posts_channel_id_idids_get

        Get Posts by ID
        """
        response = self.client.open(
            '/Middleware/API-Gateway/1.0.0/api/v1/posts/{channel_id}/id={ids}'.format(ids=56, channel_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
