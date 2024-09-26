import datetime

import pydantic

from src.models.schemas.base import BaseSchemaModel


class PresignedUploadUrl(BaseSchemaModel):    
    bucket_name: str
    file_name: str | None
    expiration: int 
    content_type: str | None
    
    