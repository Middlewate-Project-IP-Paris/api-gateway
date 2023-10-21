# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.scheduler_create_body import SchedulerCreateBody  # noqa: E501
from swagger_server.models.scheduler_update_body import SchedulerUpdateBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSchedulersController(BaseTestCase):
    """SchedulersController integration test stubs"""

    def test_api_v1_scheduler_create_post(self):
        """Test case for api_v1_scheduler_create_post

        Create scheduler
        """
        body = SchedulerCreateBody()
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/scheduler/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_scheduler_get_all_get(self):
        """Test case for api_v1_scheduler_get_all_get

        Get all the schedulers
        """
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/scheduler/get_all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_scheduler_update_put(self):
        """Test case for api_v1_scheduler_update_put

        Create scheduler
        """
        body = SchedulerUpdateBody()
        response = self.client.open(
            '/MiddleWare/API-Gateway/1.0.0/api/v1/scheduler/update',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
