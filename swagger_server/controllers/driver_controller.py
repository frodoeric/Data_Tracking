import connexion
import json
import logging

from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError
from schemas.schemas import DriverSchema
from services.services import DriverService, CustomerService
from models.entities import Driver

from swagger_server.models.create_driver_request import CreateDriverRequest  # noqa: E501
from swagger_server.models.create_driver_response import CreateDriverResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_driver_response import GetDriverResponse  # noqa: E501
from swagger_server.models.list_drivers_response import ListDriversResponse  # noqa: E501
from swagger_server.models.update_driver_request import UpdateDriverRequest  # noqa: E501


customer_service = CustomerService()
driver_service = DriverService()
driver_schema = DriverSchema()


def create_driver(body):  # noqa: E501
    """Create new Driver

    This operation is usedto create a new Driver on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateDriverResponse
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="DRV002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateDriverRequest.from_dict(connexion.request.get_json())  # noqa: E501

        customer = customer_service.fetch_by_id(body.customer_id)
        if customer is None:
            raise EntityNotFound(code="DRV003", message="Customer not found",
                                 details=f"Unable to find Customer ID {body.customer_id}")

        entity = Driver(driver_id=None, customer=customer, name=body.name, phone=body.phone, mail=body.mail)
        entity = driver_service.save(entity)
        response = CreateDriverResponse.from_dict(json.loads(driver_schema.dumps(entity)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        logging.exception("error on create driver {}", e)
        response = ErrorResponse(code="DRV0002", type=ErrorTypeEnum.UNKNOWN,
                                 message="Error on create new Driver", details=str(e))
        response_code = 500

    return response.to_dict(), response_code


def delete_driver(driver_id):  # noqa: E501
    """Delete Driver

    This operation is delete a Driver. # noqa: E501

    :param driver_id: Unique identifier of the Driver in the database
    :type driver_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        entity = driver_service.fetch_by_id(driver_id)
        if entity is None:
            raise EntityNotFound(code="DRV001", message="Driver not found",
                                 details=f"Unable to find driver ID {driver_id}")
        driver_service.delete(driver_id)
        response_code = 204

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="DRV999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code


def get_driver(driver_id):  # noqa: E501
    """Get a single Driver&#x27;s info

    This operation is used to retrieve the details of a specific device. # noqa: E501

    :param driver_id: Unique identifier of the Driver in the database
    :type driver_id: dict | bytes

    :rtype: GetDriverResponse
    """
    response = None
    response_code = None
    try:
        entity = driver_service.fetch_by_id(entity_id=driver_id)
        if entity is None:
            raise EntityNotFound(code="DRV001", message="Driver not found",
                                 details=f"Unable to find driver ID {driver_id}")
        response = GetDriverResponse.from_dict(json.loads(driver_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_drivers():  # noqa: E501
    """Get Drivers list

    This operation is used to retrieve a list of Drivers. # noqa: E501


    :rtype: ListDriversResponse
    """
    entities = driver_service.fetch_all()

    drivers_response_list = []
    for entity in entities:
        drivers_response_list.append(GetDriverResponse.from_dict(json.loads(driver_schema.dumps(entity))))

    response = ListDriversResponse(content=drivers_response_list, total_results=len(drivers_response_list))
    return response.to_dict(), 200


def update_driver(body, driver_id):  # noqa: E501
    """Update Driver&#x27;s attributes

    This operation is used to update some of the Driver&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param driver_id: Unique identifier of the Driver in the database
    :type driver_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="DRV002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateDriverRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = driver_service.fetch_by_id(driver_id)
        if entity is None:
            raise EntityNotFound(code="DRV001", message="Driver not found",
                                 details=f"Unable to find driver ID {driver_id}")

        customer = customer_service.fetch_by_id(body.customer_id)
        if customer is None:
            raise EntityNotFound(code="DRV003", message="Customer not found",
                                 details=f"Unable to find Customer ID {driver_id}")

        entity.customer = customer
        entity.name = body.name
        entity.phone = body.phone
        entity.mail = body.mail
        driver_service.save(entity)
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
