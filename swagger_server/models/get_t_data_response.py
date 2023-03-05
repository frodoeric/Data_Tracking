# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class GetTDataResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tdata_id: str=None, vehicle_id: str=None):  # noqa: E501
        """GetTDataResponse - a model defined in Swagger

        :param tdata_id: The tdata_id of this GetTDataResponse.  # noqa: E501
        :type tdata_id: str
        :param vehicle_id: The vehicle_id of this GetTDataResponse.  # noqa: E501
        :type vehicle_id: str
        """
        self.swagger_types = {
            'tdata_id': str,
            'vehicle_id': str
        }

        self.attribute_map = {
            'tdata_id': 'tdataId',
            'vehicle_id': 'vehicleId'
        }
        self._tdata_id = tdata_id
        self._vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, dikt) -> 'GetTDataResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetTDataResponse of this GetTDataResponse.  # noqa: E501
        :rtype: GetTDataResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tdata_id(self) -> str:
        """Gets the tdata_id of this GetTDataResponse.


        :return: The tdata_id of this GetTDataResponse.
        :rtype: str
        """
        return self._tdata_id

    @tdata_id.setter
    def tdata_id(self, tdata_id: str):
        """Sets the tdata_id of this GetTDataResponse.


        :param tdata_id: The tdata_id of this GetTDataResponse.
        :type tdata_id: str
        """
        if tdata_id is None:
            raise ValueError("Invalid value for `tdata_id`, must not be `None`")  # noqa: E501

        self._tdata_id = tdata_id

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this GetTDataResponse.


        :return: The vehicle_id of this GetTDataResponse.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this GetTDataResponse.


        :param vehicle_id: The vehicle_id of this GetTDataResponse.
        :type vehicle_id: str
        """
        if vehicle_id is None:
            raise ValueError("Invalid value for `vehicle_id`, must not be `None`")  # noqa: E501

        self._vehicle_id = vehicle_id
