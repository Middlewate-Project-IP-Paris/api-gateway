# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Apiv1historyhistoryDataididsMeasurements(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _date: str=None, value: int=None):  # noqa: E501
        """Apiv1historyhistoryDataididsMeasurements - a model defined in Swagger

        :param _date: The _date of this Apiv1historyhistoryDataididsMeasurements.  # noqa: E501
        :type _date: str
        :param value: The value of this Apiv1historyhistoryDataididsMeasurements.  # noqa: E501
        :type value: int
        """
        self.swagger_types = {
            '_date': str,
            'value': int
        }

        self.attribute_map = {
            '_date': 'date',
            'value': 'value'
        }
        self.__date = _date
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Apiv1historyhistoryDataididsMeasurements':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiv1historyhistory_dataidids_measurements of this Apiv1historyhistoryDataididsMeasurements.  # noqa: E501
        :rtype: Apiv1historyhistoryDataididsMeasurements
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self) -> str:
        """Gets the _date of this Apiv1historyhistoryDataididsMeasurements.


        :return: The _date of this Apiv1historyhistoryDataididsMeasurements.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this Apiv1historyhistoryDataididsMeasurements.


        :param _date: The _date of this Apiv1historyhistoryDataididsMeasurements.
        :type _date: str
        """

        self.__date = _date

    @property
    def value(self) -> int:
        """Gets the value of this Apiv1historyhistoryDataididsMeasurements.


        :return: The value of this Apiv1historyhistoryDataididsMeasurements.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this Apiv1historyhistoryDataididsMeasurements.


        :param value: The value of this Apiv1historyhistoryDataididsMeasurements.
        :type value: int
        """

        self._value = value
