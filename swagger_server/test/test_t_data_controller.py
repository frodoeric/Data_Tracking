# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_t_data_request import CreateTDataRequest  # noqa: E501
from swagger_server.models.create_t_data_response import CreateTDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_t_data_response import GetTDataResponse  # noqa: E501
from swagger_server.models.list_t_datas_response import ListTDatasResponse  # noqa: E501
from swagger_server.models.update_t_data_request import UpdateTDataRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTDataController(BaseTestCase):
    """TDataController integration test stubs"""

    def test_create_tdata(self):
        """Test case for create_tdata

        Create new Data
        """
        body = CreateTDataRequest()
        response = self.client.open(
            '/tracking/tdata',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_tdata(self):
        """Test case for delete_tdata

        Delete Customer
        """
        response = self.client.open(
            '/tracking/tdata/{tdataId}'.format(tdata_id='tdata_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tdata(self):
        """Test case for get_tdata

        Get a single TData's info
        """
        response = self.client.open(
            '/tracking/tdata/{tdataId}'.format(tdata_id='tdata_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_tdatas(self):
        """Test case for list_tdatas

        Get Data list
        """
        response = self.client.open(
            '/tracking/tdata',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_tdata(self):
        """Test case for update_tdata

        Update Data's attributes
        """
        body = UpdateTDataRequest()
        response = self.client.open(
            '/tracking/tdata/{tdataId}'.format(tdata_id='tdata_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
