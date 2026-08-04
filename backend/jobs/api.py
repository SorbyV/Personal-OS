from fastapi import APIRouter
router = APIRouter(prefix="/job", tags=["job"])

@router.get("/")
async def root():
    return {"message":"Welcome to the jobs section!"}
@router.get("/{item}")
async def get_item(item):
    return {item: "The Job id is "+item}