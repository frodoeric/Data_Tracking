from flask_marshmallow.fields import fields

from config import ma
from models.entities import Data
from typing import List


class DataSchema(ma.SQLAlchemyAutoSchema):
    customerId = fields.String(attribute="data_id")

    class Meta:
        model = Data
        load_instance = True
        exclude = ["data_id"]
