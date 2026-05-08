from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# 创建一个 FastAPI 实例
app = FastAPI()
items_db: list[dict] = []
# 定义一个路由（endpoint）
@app.get("/")
def read_root():
    return {"message": "Hello World"}
@app.get("/info")
def get_info():
    return {
        "project": "智能文档问答系统",
        "version": "0.1.0",
        "status": "开发中"
    }

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
# POST 创建
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.model_dump()
    items_db.append(item_dict)
    return {"message": "创建成功", "item": item_dict, "total": len(items_db)}

# GET 列表（分页查询参数）
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "data": items_db[skip : skip + limit],
        "total": len(items_db),
        "skip": skip,
        "limit": limit
    }

# GET 单个（路径参数，必须放最后）
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        return {"error": "找不到这个物品"}
    return {"item": items_db[item_id]}