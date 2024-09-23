import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.model import Model 
from src.models.schemas.model import ModelInResponse
from src.repository.crud.base import BaseCRUDRepository

import loguru
class ModelCRUDRepository(BaseCRUDRepository):
    async def read_models(self) -> typing.Sequence[Model]:
        stmt = sqlalchemy.select(Model)
        
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()
