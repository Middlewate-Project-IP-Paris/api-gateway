# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, post_id: int=None, name: str=None, link: str=None, description: str=None, subs: int=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger

        :param post_id: The post_id of this InlineResponse2003.  # noqa: E501
        :type post_id: int
        :param name: The name of this InlineResponse2003.  # noqa: E501
        :type name: str
        :param link: The link of this InlineResponse2003.  # noqa: E501
        :type link: str
        :param description: The description of this InlineResponse2003.  # noqa: E501
        :type description: str
        :param subs: The subs of this InlineResponse2003.  # noqa: E501
        :type subs: int
        """
        self.swagger_types = {
            'post_id': int,
            'name': str,
            'link': str,
            'description': str,
            'subs': int
        }

        self.attribute_map = {
            'post_id': 'post_id',
            'name': 'name',
            'link': 'link',
            'description': 'description',
            'subs': 'subs'
        }
        self._post_id = post_id
        self._name = name
        self._link = link
        self._description = description
        self._subs = subs

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def post_id(self) -> int:
        """Gets the post_id of this InlineResponse2003.


        :return: The post_id of this InlineResponse2003.
        :rtype: int
        """
        return self._post_id

    @post_id.setter
    def post_id(self, post_id: int):
        """Sets the post_id of this InlineResponse2003.


        :param post_id: The post_id of this InlineResponse2003.
        :type post_id: int
        """

        self._post_id = post_id

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse2003.


        :return: The name of this InlineResponse2003.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse2003.


        :param name: The name of this InlineResponse2003.
        :type name: str
        """

        self._name = name

    @property
    def link(self) -> str:
        """Gets the link of this InlineResponse2003.


        :return: The link of this InlineResponse2003.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link: str):
        """Sets the link of this InlineResponse2003.


        :param link: The link of this InlineResponse2003.
        :type link: str
        """

        self._link = link

    @property
    def description(self) -> str:
        """Gets the description of this InlineResponse2003.


        :return: The description of this InlineResponse2003.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InlineResponse2003.


        :param description: The description of this InlineResponse2003.
        :type description: str
        """

        self._description = description

    @property
    def subs(self) -> int:
        """Gets the subs of this InlineResponse2003.


        :return: The subs of this InlineResponse2003.
        :rtype: int
        """
        return self._subs

    @subs.setter
    def subs(self, subs: int):
        """Sets the subs of this InlineResponse2003.


        :param subs: The subs of this InlineResponse2003.
        :type subs: int
        """

        self._subs = subs