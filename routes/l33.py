from fastapi import APIRouter, Body

from database.database import *
from models.l33 import *

router: APIRouter = APIRouter()


@router.get("/", response_description="L33_2p data retrieved", response_model=Response)
async def get_l33_2p_list():
    l33_2p_data = await retrieve_l33_2p_list()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "L33_2p data retrieved successfully",
        "data": l33_2p_data,
    }


@router.get(
    "/{id}", response_description="L33_2p data retrieved", response_model=Response
)
async def get_l33_2p_by_id(id: PydanticObjectId):
    l33_2p = await retrieve_l33_2p_by_id(id)
    if l33_2p:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "L33_2p data retrieved successfully",
            "data": l33_2p,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "L33_2p doesn't exist",
    }


@router.post(
    "/", response_description="L33_2p data added into the database", response_model=Response
)
async def add_l33_2p_data(l33_2p: L33_2p = Body(...)):
    new_l33_2p = await add_l33_2p(l33_2p)
    if new_l33_2p is not None:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "L33_2p created successfully",
            "data": new_l33_2p,
        }
    else:
        return {
            "status_code": 400,
            "response_type": "error",
            "description": "L33_2p with the specified issue already exists",
            "data": None,
        }


@router.delete("/{id}", response_description="L33_2p data deleted from the database")
async def delete_l33_2p_data(id: PydanticObjectId):
    deleted_l33_2p = await delete_l33_2p(id)
    if deleted_l33_2p:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "L33_2p with ID: {} removed".format(id),
            "data": deleted_l33_2p,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "L33_2p with id {0} doesn't exist".format(id),
        "data": False,
    }

@router.put("/{id}", response_model=Response)
async def update_l33_2p(id: PydanticObjectId, req: UpdateL33_2pModel = Body(...)):
    updated_l33_2p = await update_l33_2p_data(id, req.dict())
    if updated_l33_2p:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "L33_2p with ID: {} updated".format(id),
            "data": updated_l33_2p,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. L33_2p with ID: {} not found".format(id),
        "data": False,
    }