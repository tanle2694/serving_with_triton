import datetime

import pydantic

from src.models.schemas.base import BaseSchemaModel



class ModelInCreate(BaseSchemaModel):    
    name: str
    type: str | None
    description: str | None    
    
    

class ModelInResponse(BaseSchemaModel):
    id: int
    name: str
    type: str | None
    description: str | None
    status: str | None
    last_active: datetime.datetime | None
    created_at: datetime.datetime 
    

class ModelAfterCreate(BaseSchemaModel):
    id: int
    name: str
    type: str | None
    description: str | None        
    created_at: datetime.datetime | None
    