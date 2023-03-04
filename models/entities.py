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

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), unique=True)
    mail = db.Column(db.String(255))

    def get_id(self):
        return self.customer_id

    def __init__(self, customer_id, name, phone, mail):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.mail = mail

    def __repr__(self):
        return 'Customer(customer_id=%d, name=%s, phone=%s, mail=%s)' % (
            self.customer_id, self.name, self.phone, self.mail)

    def json(self):
        return {'customer_id': str(self.customer_id), 'name': self.name, 'phone': self.phone, 'mail': self.mail}


class Driver(db.Model):
    __tablename__ = "drivers"

    driver_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = db.Column(UUID(as_uuid=True), db.ForeignKey("customers.customer_id"))
    name = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), unique=True)
    mail = db.Column(db.String(255))

    customer = relationship("Customer")

    def get_id(self):
        return self.driver_id

    def __init__(self, driver_id, customer, name, phone, mail):
        self.driver_id = driver_id
        self.customer = customer
        self.name = name
        self.phone = phone
        self.mail = mail

    def __repr__(self):
        return 'Driver(driver_id=%d, name=%s, customer=%s, phone=%s, mail=%s)' % (self.driver_id, self.customer,
                                                                                  self.name, self.phone, self.mail)

    def json(self):
        return {'id': str(self.driver_id), 'customer_id': str(self.customer.customer_id), 'name': self.name, 'phone': self.phone,
                'mail': self.mail}
