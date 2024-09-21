import fastapi
import pydantic

router = fastapi.APIRouter(prefix="/hello", tags=["hello"])


@router.get(
    path="",
    name="hello",
    response_model=str,
    status_code=fastapi.status.HTTP_200_OK,
)
async def hello_get() -> list[pydantic.BaseModel]:
    return "hello"

