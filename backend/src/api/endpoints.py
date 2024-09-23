import fastapi

from src.api.routes.hello import router as hello_router
from src.api.routes.model import router as model_list_router

router = fastapi.APIRouter()


router.include_router(router=hello_router)
router.include_router(router=model_list_router)
