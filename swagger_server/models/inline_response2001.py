# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.apiv1historyhistory_dataidids_measurements import Apiv1historyhistoryDataididsMeasurements  # noqa: F401,E501
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel_id: int=None, measurements: Apiv1historyhistoryDataididsMeasurements=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param channel_id: The channel_id of this InlineResponse2001.  # noqa: E501
        :type channel_id: int
        :param measurements: The measurements of this InlineResponse2001.  # noqa: E501
        :type measurements: Apiv1historyhistoryDataididsMeasurements
        """
        self.swagger_types = {
            'channel_id': int,
            'measurements': Apiv1historyhistoryDataididsMeasurements
        }

        self.attribute_map = {
            'channel_id': 'channel_id',
            'measurements': 'measurements'
        }
        self._channel_id = channel_id
        self._measurements = measurements

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel_id(self) -> int:
        """Gets the channel_id of this InlineResponse2001.


        :return: The channel_id of this InlineResponse2001.
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id: int):
        """Sets the channel_id of this InlineResponse2001.


        :param channel_id: The channel_id of this InlineResponse2001.
        :type channel_id: int
        """

        self._channel_id = channel_id

    @property
    def measurements(self) -> Apiv1historyhistoryDataididsMeasurements:
        """Gets the measurements of this InlineResponse2001.


        :return: The measurements of this InlineResponse2001.
        :rtype: Apiv1historyhistoryDataididsMeasurements
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements: Apiv1historyhistoryDataididsMeasurements):
        """Sets the measurements of this InlineResponse2001.


        :param measurements: The measurements of this InlineResponse2001.
        :type measurements: Apiv1historyhistoryDataididsMeasurements
        """

        self._measurements = measurements
