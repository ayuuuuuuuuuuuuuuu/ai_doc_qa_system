from fastapi import FastAPI

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