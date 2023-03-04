from models.entities import Customer, Driver, TData
from models.repositories import BaseRepository, CustomerRepository, DriverRepository, TDataRepository
from typing import List, Type


class BaseService:

    repository: BaseRepository = NotImplementedError
    entity: Type = NotImplementedError

    def fetch_by_id(self, entity_id) -> entity:
        return self.repository.fetch_by_id(entity_id)

    def fetch_all(self) -> List[entity]:
        return self.repository.fetch_all()

    def save(self, entity) -> entity:
        return self.repository.create(entity)

    def update(self, entity) -> entity:
        return self.repository.update(entity)

    def delete(self, entity_id) -> None:
        self.repository.delete(entity_id)


class TDataService(BaseService):

    def __init__(self):
        self.repository = TDataRepository()
        self.entity = TData

class CustomerService (BaseService):

    def __init__(self):
        self.repository = CustomerRepository()
        self.entity = Customer


class DriverService(BaseService):

    def __init__(self):
        self.repository = DriverRepository()
        self.entity = Driver
