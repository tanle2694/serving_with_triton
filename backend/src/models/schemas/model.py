import datetime

import pydantic

from src.models.schemas.base import BaseSchemaModel



class ModelInCreate(BaseSchemaModel):    
    name: str
    type: str | None
    description: str | None
    model_path: str
    

class ModelInResponse(BaseSchemaModel):
    id: int
    name: str
    type: str | None
    description: str | None
    status: str
    last_active: datetime.datetime | None
    created_at: datetime.datetime
    
    
