from fastapi import APIRouter

router = APIRouter()

@router.get("/programs/{organization_id}")
async def get_programs(organization_id: str):
    return { 'endpoint': 'programs' }