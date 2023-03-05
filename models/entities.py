from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Data(db.Model):

    __tablename__ = "data"

    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    data_hora = db.Column(db.DateTime, default=now)

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle_id, data_hora):
        self.data_id = data_id
        self.vehicle_id = vehicle_id
        self.data_hora = data_hora

    def json(self):
        return {'data_id': str(self.data_id), 'vehicle_id': self.vehicle_id, 'data_hora': self.data_hora}