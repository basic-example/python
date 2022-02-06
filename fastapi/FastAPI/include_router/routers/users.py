from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_list():
    return {"data": [{"id": 1, "name": "yoo"}]}
