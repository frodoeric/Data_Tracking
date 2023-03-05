from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TData(db.Model):
    __tablename__ = "tdata"

    tdata_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    data_hora = db.Column(db.DateTime, default=now)

    def get_id(self):
        return self.tdata_id

    def __init__(self, tdata_id, vehicle_id, data_hora):
        self.tdata_id = tdata_id
        self.vehicle_id = vehicle_id
        self.data_hora = data_hora

    def __repr__(self):
        return 'Customer(tdata_id=%d, vehicle_id=%s, data_hora=%s)' % (
            self.tdata_id, self.vehicle_id, self.data_hora)

    def json(self):
        return {'tdata_id': str(self.tdata_id), 'vehicle_id': self.vehicle_id, 'data_hora': self.data_hora}