from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter()


programs = {
    'abc123': {'programId': 'abc123', 'programName': 'Program 1 Description',
               'programDescription': 'Program 1'},
    'abc456': {'programId': 'abc456', 'programName': 'Program 2 Description',
               'programDescription': 'Program 2 Description'},
    'abc789': {'programId': 'abc789', 'programName': 'Program 3',
               'programDescription': 'Program 3 Description'},
}


class Program(BaseModel):
    programId: str
    programName: str
    programDescription: Optional[str] = None


@router.get("/programs/{organization_id}", response_model=Program)
async def get_programs(organization_id: str, program_id: Optional[str] = None):
    table_name = f'programs_{organization_id}'
    if program_id:
        return programs[program_id]
    return {'table name': f'{table_name}'}
