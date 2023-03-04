from flask_marshmallow.fields import fields

from config import ma
from models.entities import Customer, Driver, TData
from typing import List

from swagger_server.models import CreateCustomerResponse

class TDataSchema(ma.SQLAlchemyAutoSchema):
    customerId = fields.String(attribute="tdata_id")

    class Meta:
        model = TData
        load_instance = True
        exclude = ["tdata_id"]

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    customerId = fields.String(attribute="customer_id")

    class Meta:
        model = Customer
        load_instance = True
        exclude = ["customer_id"]


class DriverSchema(ma.SQLAlchemyAutoSchema):
    driverId = fields.String(attribute="driver_id")
    customerId = fields.String(attribute="customer_id")

    class Meta:
        model = Driver
        load_instance = True
        exclude = ["driver_id", "customer_id"]
