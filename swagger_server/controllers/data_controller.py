import json

import connexion
import six
import datetime
from custom_errors import InvalidPayload, BaseCustomError, EntityNotFound
from models.entities import Data
from schemas.schemas import DataSchema
from services.services import DataService
from swagger_server.models import ErrorTypeEnum
from swagger_server.models.create_data_request import CreateDataRequest  # noqa: E501
from swagger_server.models.create_data_response import CreateDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_data_response import GetDataResponse  # noqa: E501
from swagger_server.models.list_datas_response import ListDatasResponse  # noqa: E501
from swagger_server.models.update_data_request import UpdateDataRequest  # noqa: E501
from swagger_server import util

data_service = DataService()
data_schema = DataSchema()

def create_data(body):  # noqa: E501
    """Create new Data

    This operation is used to create a new Data Telemetry on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateDataResponse
    """

    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = Data(data_id=None, vehicle_id=body.vehicle_id, data_hora=datetime.datetime.now())
        entity = data_service.save(entity)
        response = CreateDataResponse.from_dict(json.loads(data_schema.dumps(entity)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new Customer", details=str(e))

    return response.to_dict(), response_code


def delete_data(data_id):  # noqa: E501
    """Delete Customer

    This operation is delete a Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        entity = data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {data_id}")
        data_service.delete(data_id)
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


def get_data(data_id):  # noqa: E501
    """Get a single Data&#x27;s info

    This operation is used to retrieve the details of a specific Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetDataResponse
    """
    response = None
    response_code = None
    try:
        entity = data_service.fetch_by_id(entity_id=data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {data_id}")
        response = GetDataResponse.from_dict(json.loads(data_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_datas():  # noqa: E501
    """Get Data list

    This operation is used to retrieve a list of Telemetry Data. # noqa: E501


    :rtype: ListDatasResponse
    """
    entities = data_service.fetch_all()

    data_response_list = []
    for entity in entities:
        data_response_list.append(GetDataResponse.from_dict(json.loads(data_schema.dumps(entity))))

    response = ListDatasResponse(content=data_response_list, total_results=len(data_response_list))

    return response.to_dict(), 200

def update_data(body, data_id):  # noqa: E501
    """Update Data&#x27;s attributes

    This operation is used to update some of the Data&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Customer not found",
                                 details=f"Unable to find customer ID {data_id}")
        entity.vehicle_id = body.vehicleId
        entity.data_hora = datetime.datetime.now()
        data_service.save(entity)
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
