from fastapi import APIRouter
import json
from . import manager

router = APIRouter(prefix="/job", tags=["job"])
@router.get("/")
async def root():
    return {"message":"Welcome to the jobs section!"}
@router.get("/{item}")
async def get_item(item):
    return {item: "The Job id is "+item}

@router.post("/{item}")
async def post_job(item):
    sample_job = {
        "id": item,
        "company": str(item),
        "job_title": "sample job title",
        "location": "Bangalore",
    }
    json_output = json.dumps(manager.create_job(sample_job))
    return json_output


@router.post("/wrong_job/{item}")
async def post_wrong_job(item):
    sample_job = {
        "id": item,
        "company": "",
        "job_title": "sample job title",
        "location": "Bangalore",
    }
    json_output = json.dumps(manager.create_job(sample_job))
    return json_output