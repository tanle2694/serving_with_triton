
import fastapi

from src.models.schemas.storage import PresignedUploadUrl

router = fastapi.APIRouter(prefix="/storage", tags=["storage"])



@router.get(
    path="/presigned-upload-url",
    name="storage:presigned-upload-url",
    response_model=str,
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_presigned_upload_url(
        presigned_upload_url: PresignedUploadUrl,
) -> str:
    
