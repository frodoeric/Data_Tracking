import connexion
import json

from models.entities import TData
from services.services import TDataService
from schemas.schemas import TDataSchema
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError


customer_service = TDataService()
customer_schema = TDataSchema()


def create_tdata(body):  # noqa: E501
    """Create new DAta

    This operation is used to create a new Data on System. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: CreateCustomerResponse
    """
    response = None
    response_code = None


def delete_tdata(tdata_id):  # noqa: E501
    """Delete Customer

    This operation is delete a Customer. # noqa: E501

    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: None
    """



def get_tdata(tdata_id):  # noqa: E501
    """Get a single Customer&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: GetCustomerResponse
    """


def list_tdatas():  # noqa: E501
    """Get Customers list

    This operation is used to retrieve a list of Customers. # noqa: E501


    :rtype: ListCustomersResponse
    """



def update_tdata(body, customer_id):  # noqa: E501
    """Update Customer&#x27;s attributes

    This operation is used to update some of the Customer&#x27;s attributes. # noqa: E501

    :param body:
    :type body: dict | bytes
    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: None
    """
