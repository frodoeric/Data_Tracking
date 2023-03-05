import connexion
import six

from swagger_server.models.create_t_data_request import CreateTDataRequest  # noqa: E501
from swagger_server.models.create_t_data_response import CreateTDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_t_data_response import GetTDataResponse  # noqa: E501
from swagger_server.models.list_t_datas_response import ListTDatasResponse  # noqa: E501
from swagger_server.models.update_t_data_request import UpdateTDataRequest  # noqa: E501
from swagger_server import util


def create_tdata(body):  # noqa: E501
    """Create new Data

    This operation is used to create a new Data Telemetry on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateTDataResponse
    """
    if connexion.request.is_json:
        body = CreateTDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_tdata(tdata_id):  # noqa: E501
    """Delete Customer

    This operation is delete a Data. # noqa: E501

    :param tdata_id: Unique identifier of the Data in the database
    :type tdata_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tdata_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_tdata(tdata_id):  # noqa: E501
    """Get a single TData&#x27;s info

    This operation is used to retrieve the details of a specific Data. # noqa: E501

    :param tdata_id: Unique identifier of the Data in the database
    :type tdata_id: dict | bytes

    :rtype: GetTDataResponse
    """
    if connexion.request.is_json:
        tdata_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_tdatas():  # noqa: E501
    """Get Data list

    This operation is used to retrieve a list of Telemetry Data. # noqa: E501


    :rtype: ListTDatasResponse
    """
    return 'do some magic!'


def update_tdata(body, tdata_id):  # noqa: E501
    """Update Data&#x27;s attributes

    This operation is used to update some of the Data&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param tdata_id: Unique identifier of the Data in the database
    :type tdata_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateTDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        tdata_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
