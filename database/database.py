from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.l33 import L33_2p

admin_collection = Admin
l33_2p_collection = L33_2p


async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


async def retrieve_l33_2p_list() -> List[L33_2p]:
    l33_2p_list = await l33_2p_collection.find().sort([("issue", -1)]).limit(30).to_list(30)
    return l33_2p_list



async def add_l33_2p(new_l33_2p: L33_2p) -> L33_2p:
    existing_issue = await l33_2p_collection.find_one({"issue": new_l33_2p.issue})

    if existing_issue is None:
        l33_2p = await new_l33_2p.create()
        return l33_2p
    else:
        return None


async def retrieve_l33_2p_by_id(id: PydanticObjectId) -> L33_2p:
    l33_2p = await l33_2p_collection.get(id)
    if l33_2p:
        return l33_2p


async def delete_l33_2p(id: PydanticObjectId) -> bool:
    l33_2p = await l33_2p_collection.get(id)
    if l33_2p:
        await l33_2p.delete()
        return True
    return False


async def update_l33_2p_data(id: PydanticObjectId, data: dict) -> Union[bool, L33_2p]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    l33_2p = await l33_2p_collection.get(id)
    if l33_2p:
        await l33_2p.update(update_query)
        return l33_2p
    return False
