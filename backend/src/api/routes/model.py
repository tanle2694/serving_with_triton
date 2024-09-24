import fastapi
import pydantic
from typing import List
from src.repository.crud.model import ModelCRUDRepository
from src.models.schemas.model import ModelInResponse, ModelInCreate
from src.api.dependencies.repository import get_repository
import loguru
import datetime

router = fastapi.APIRouter(prefix="/models", tags=["models"])


@router.get(
    path="",
    name="modelss:read-models",
    response_model=List[ModelInResponse],
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_accounts(
    model_repo: ModelCRUDRepository = fastapi.Depends(get_repository(repo_type=ModelCRUDRepository)),
) -> list[ModelInResponse]:
    loguru.logger.info("Getting models")
    db_models = await model_repo.read_models()    
    db_model_list: list[ModelInResponse] = list()

    for db_model in db_models:        
        model = ModelInResponse(
            id=db_model.id,
            name=db_model.name,
            type=db_model.type,
            description=db_model.description,
            status=db_model.status,
            last_active=db_model.last_active,
            created_at=db_model.created_at
        )      
        db_model_list.append(model)

    return db_model_list


@router.post(
    path="",
    name="modelss:create-model",
    response_model=ModelInResponse,
    status_code=fastapi.status.HTTP_200_OK,
)
async def upload_model(
        model_create: ModelInCreate,
        model_repo: ModelCRUDRepository = fastapi.Depends(get_repository(repo_type=ModelCRUDRepository)),
) -> ModelInResponse:
    loguru.logger.info("Creating model")
    db_model = await model_repo.create_model(model_create)
    return ModelInResponse(
        id=db_model.id,
        name=db_model.name,
        type=db_model.type,
        description=db_model.description,
        status=db_model.status,
    )


