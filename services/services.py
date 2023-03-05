from models.entities import Data
from models.repositories import BaseRepository, DataRepository
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


class DataService(BaseService):

    def __init__(self):
        self.repository = DataRepository()
        self.entity = Data

