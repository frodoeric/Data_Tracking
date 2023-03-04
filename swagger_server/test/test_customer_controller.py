# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_customer_request import CreateCustomerRequest  # noqa: E501
from swagger_server.models.create_customer_response import CreateCustomerResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_customer_response import GetCustomerResponse  # noqa: E501
from swagger_server.models.list_customers_response import ListCustomersResponse  # noqa: E501
from swagger_server.models.update_customer_request import UpdateCustomerRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_create_customer(self):
        """Test case for create_customer

        Create new Customer
        """
        body = CreateCustomerRequest()
        response = self.client.open(
            '/tracking/customers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_customer(self):
        """Test case for delete_customer

        Delete Customer
        """
        response = self.client.open(
            '/tracking/customers/{customerId}'.format(customer_id='customer_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer(self):
        """Test case for get_customer

        Get a single Customer's info
        """
        response = self.client.open(
            '/tracking/customers/{customerId}'.format(customer_id='customer_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_customers(self):
        """Test case for list_customers

        Get Customers list
        """
        response = self.client.open(
            '/tracking/customers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Update Customer's attributes
        """
        body = UpdateCustomerRequest()
        response = self.client.open(
            '/tracking/customers/{customerId}'.format(customer_id='customer_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
