# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class UpdateDataRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, vehicle_id: str=None, data_hora: datetime=None):  # noqa: E501
        """UpdateDataRequest - a model defined in Swagger

        :param vehicle_id: The vehicle_id of this UpdateDataRequest.  # noqa: E501
        :type vehicle_id: str
        :param data_hora: The data_hora of this UpdateDataRequest.  # noqa: E501
        :type data_hora: datetime
        """
        self.swagger_types = {
            'vehicle_id': str,
            'data_hora': datetime
        }

        self.attribute_map = {
            'vehicle_id': 'vehicleId',
            'data_hora': 'dataHora'
        }
        self._vehicle_id = vehicle_id
        self._data_hora = data_hora

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateDataRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateDataRequest of this UpdateDataRequest.  # noqa: E501
        :rtype: UpdateDataRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this UpdateDataRequest.


        :return: The vehicle_id of this UpdateDataRequest.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this UpdateDataRequest.


        :param vehicle_id: The vehicle_id of this UpdateDataRequest.
        :type vehicle_id: str
        """

        self._vehicle_id = vehicle_id

    @property
    def data_hora(self) -> datetime:
        """Gets the data_hora of this UpdateDataRequest.

        Data hora  # noqa: E501

        :return: The data_hora of this UpdateDataRequest.
        :rtype: datetime
        """
        return self._data_hora

    @data_hora.setter
    def data_hora(self, data_hora: datetime):
        """Sets the data_hora of this UpdateDataRequest.

        Data hora  # noqa: E501

        :param data_hora: The data_hora of this UpdateDataRequest.
        :type data_hora: datetime
        """

        self._data_hora = data_hora
