# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_driver_request import CreateDriverRequest  # noqa: E501
from swagger_server.models.create_driver_response import CreateDriverResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_driver_response import GetDriverResponse  # noqa: E501
from swagger_server.models.list_drivers_response import ListDriversResponse  # noqa: E501
from swagger_server.models.update_driver_request import UpdateDriverRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDriverController(BaseTestCase):
    """DriverController integration test stubs"""

    def test_create_driver(self):
        """Test case for create_driver

        Create new Driver
        """
        body = CreateDriverRequest()
        response = self.client.open(
            '/tracking/drivers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_driver(self):
        """Test case for delete_driver

        Delete Driver
        """
        response = self.client.open(
            '/tracking/drivers/{driverId}'.format(driver_id='driver_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver(self):
        """Test case for get_driver

        Get a single Driver's info
        """
        response = self.client.open(
            '/tracking/drivers/{driverId}'.format(driver_id='driver_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_drivers(self):
        """Test case for list_drivers

        Get Drivers list
        """
        response = self.client.open(
            '/tracking/drivers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_driver(self):
        """Test case for update_driver

        Update Driver's attributes
        """
        body = UpdateDriverRequest()
        response = self.client.open(
            '/tracking/drivers/{driverId}'.format(driver_id='driver_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
