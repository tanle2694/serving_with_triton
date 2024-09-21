import fastapi

from src.api.routes.hello import router as hello_router
router = fastapi.APIRouter()


router.include_router(router=hello_router)
