import connexion
import json

from models.entities import Customer
from services.services import CustomerService
from schemas.schemas import CustomerSchema
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_customer_request import CreateCustomerRequest  # noqa: E501
from swagger_server.models.create_customer_response import CreateCustomerResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_customer_response import GetCustomerResponse  # noqa: E501
from swagger_server.models.list_customers_response import ListCustomersResponse  # noqa: E501
from swagger_server.models.update_customer_request import UpdateCustomerRequest  # noqa: E501


customer_service = CustomerService()
customer_schema = CustomerSchema()


def create_customer(body):  # noqa: E501
    """Create new Customer

    This operation is usedto create a new Customer on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateCustomerResponse
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateCustomerRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = Customer(customer_id=None, name=body.name, phone=body.phone, mail=body.mail)
        entity = customer_service.save(entity)
        response = CreateCustomerResponse.from_dict(json.loads(customer_schema.dumps(entity)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new Customer", details=str(e))

    return response.to_dict(), response_code


def delete_customer(customer_id):  # noqa: E501
    """Delete Customer

    This operation is delete a Customer. # noqa: E501

    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        entity = customer_service.fetch_by_id(customer_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {customer_id}")
        customer_service.delete(customer_id)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code


def get_customer(customer_id):  # noqa: E501
    """Get a single Customer&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: GetCustomerResponse
    """
    response = None
    response_code = None
    try:
        entity = customer_service.fetch_by_id(entity_id=customer_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {customer_id}")
        response = GetCustomerResponse.from_dict(json.loads(customer_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_customers():  # noqa: E501
    """Get Customers list

    This operation is used to retrieve a list of Customers. # noqa: E501


    :rtype: ListCustomersResponse
    """
    entities = customer_service.fetch_all()

    customer_response_list = []
    for entity in entities:
        customer_response_list.append(GetCustomerResponse.from_dict(json.loads(customer_schema.dumps(entity))))

    response = ListCustomersResponse(content=customer_response_list, total_results=len(customer_response_list))
    return response.to_dict(), 200


def update_customer(body, customer_id):  # noqa: E501
    """Update Customer&#x27;s attributes

    This operation is used to update some of the Customer&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param customer_id: Unique identifier of the Customer in the database
    :type customer_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateCustomerRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = customer_service.fetch_by_id(customer_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {customer_id}")
        entity.name = body.name
        entity.phone = body.phone
        entity.mail = body.mail
        customer_service.save(entity)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))

    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code
