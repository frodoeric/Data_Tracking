# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_data_request import CreateDataRequest  # noqa: E501
from swagger_server.models.create_data_response import CreateDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_data_response import GetDataResponse  # noqa: E501
from swagger_server.models.list_datas_response import ListDatasResponse  # noqa: E501
from swagger_server.models.update_data_request import UpdateDataRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataController(BaseTestCase):
    """DataController integration test stubs"""

    def test_create_data(self):
        """Test case for create_data

        Create new Data
        """
        body = CreateDataRequest()
        response = self.client.open(
            '/tracking/data',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_data(self):
        """Test case for delete_data

        Delete Customer
        """
        response = self.client.open(
            '/tracking/data/{dataId}'.format(data_id='data_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data(self):
        """Test case for get_data

        Get a single Data's info
        """
        response = self.client.open(
            '/tracking/data/{dataId}'.format(data_id='data_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_datas(self):
        """Test case for list_datas

        Get Data list
        """
        response = self.client.open(
            '/tracking/data',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_data(self):
        """Test case for update_data

        Update Data's attributes
        """
        body = UpdateDataRequest()
        response = self.client.open(
            '/tracking/data/{dataId}'.format(data_id='data_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
