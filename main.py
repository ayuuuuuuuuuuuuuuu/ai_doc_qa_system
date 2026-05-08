from fastapi import FastAPI
from pydantic import BaseModel

# 创建一个 FastAPI 实例
app = FastAPI()

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
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"你查询了第 {item_id} 个物品"}

# ====== 查询参数 ======
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "data": f"返回第 {skip} 到 {skip + limit} 条数据"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  # 可选字段

# ====== POST 请求 ======
items_db = []  # 用来存所有创建的物品

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/item/")
def create_item(item: Item):
    items_db.append(item)  # ← 存到列表里
    return {"message": "创建成功", "item": item, "total": len(items_db)}

@app.get("/item/")
def read_all_items():
    return {"items": items_db, "count": len(items_db)}

@app.get("/item/{item_id}")
def read_item(item_id: int):
    if item_id < len(items_db):
        return {"item": items_db[item_id]}
    return {"error": "找不到这个物品"}