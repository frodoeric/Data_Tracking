from config import db
from models.entities import TData
from typing import List, Type


class BaseRepository:

    id_attr_name: Type = NotImplementedError
    entity_model: Type = NotImplementedError
    database: db = NotImplementedError

    def create(self, entity) -> entity_model:
        self.db.session.add(entity)
        self.db.session.commit()
        return entity

    def fetch_by_id(self, entity_id) -> entity_model:
        return self.db.session.query(self.entity_model).filter_by(**{self.id_attr_name: entity_id}).first()

    def fetch_all(self) -> List[entity_model]:
        return self.db.session.query(self.entity_model).all()

    def delete(self, entity_id) -> None:
        entity = self.db.session.query(self.entity_model).filter_by(**{self.id_attr_name: entity_id}).first()
        self.db.session.delete(entity)
        self.db.session.commit()

    def update(self, entity) -> entity_model:
        self.db.session.merge(entity)
        self.db.session.commit()
        return entity


class TDataRepository(BaseRepository):

    def __init__(self):
        self.id_attr_name = 'tdata_id'
        self.db = db
        self.entity_model = TData
