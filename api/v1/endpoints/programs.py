import json
from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel, parse_obj_as

router = APIRouter()


class Program(BaseModel):
    programId: str
    programName: str
    programDescription: Optional[str] = None


class Programs(BaseModel):
    programs: List[Program] = []


programs = [
    {'programId': 'abc123', 'programName': 'Program 1 Description',
     'programDescription': 'Program 1'},
    {'programId': 'abc456', 'programName': 'Program 2 Description',
     'programDescription': 'Program 2 Description'},
    {'programId': 'abc789', 'programName': 'Program 3',
     'programDescription': 'Program 3 Description'}
]


@router.get("/programs/{organization_id}", response_model=List[Program])
async def get_all_programs(organization_id: str):
    table_name = f'programs_{organization_id}'
    return programs


@router.get("/programs/{organization_id}/{program_id}", response_model=Program)
async def get_program(organization_id: str, program_id: str):
    table_name = f'programs_{organization_id}'
    for program in programs:
        if program['programId'] == program_id:
            return program
    return {'message': 'Not found'}
