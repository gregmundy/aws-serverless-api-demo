from fastapi import APIRouter
from .endpoints.programs import router as programs_router

router = APIRouter()
router.include_router(programs_router, tags=['ETPL Programs'])