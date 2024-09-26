import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.model import Model 
from src.models.schemas.model import ModelInResponse, ModelInCreate
from src.repository.crud.base import BaseCRUDRepository

import loguru


class ModelCRUDRepository(BaseCRUDRepository):
    async def read_models(self) -> typing.Sequence[Model]:
        stmt = sqlalchemy.select(Model)
        
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def create_model(self, model_create: ModelInCreate) -> Model:
        new_model = Model(
            name=model_create.name,
            type=model_create.type,
            description=model_create.description
        )
        self.async_session.add(instance=new_model)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_model)
        # stmt = sqlalchemy.insert(Model).values(
        #     name=model_create.name,
        #     type=model_create.type,
        #     description=model_create.description            
        # )

        # model_created = await self.async_session.execute(statement=stmt)
        return new_model