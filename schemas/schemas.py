from flask_marshmallow.fields import fields

from config import ma
from models.entities import TData
from typing import List


class TDataSchema(ma.SQLAlchemyAutoSchema):
    customerId = fields.String(attribute="tdata_id")

    class Meta:
        model = TData
        load_instance = True
        exclude = ["tdata_id"]
