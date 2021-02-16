from fastapi import APIRouter
from api.v1.endpoints.programs import router as programs_router

router = APIRouter()
router.include_router(programs_router, tags=['ETPL Programs'])