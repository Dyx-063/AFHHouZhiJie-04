from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# 加载.env配置文件
load_dotenv()
app = FastAPI(title="AI问答后端服务")

# 解决前端跨域问题，必须配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义请求体格式
class ChatRequest(BaseModel):
    question: str

# 读取Dify配置
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_API_URL = os.getenv("DIFY_API_URL")

# 接收前端POST JSON参数
@app.post("/chat")
def chat(req: ChatRequest):
    import traceback
    try:
        question = req.question
        headers = {
            "Authorization": f"Bearer {DIFY_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": {},
            "query": question,
            "response_mode": "blocking",
            "user": "local-user"
        }
        resp = requests.post(DIFY_API_URL, headers=headers, json=payload, timeout=30)
        resp_data = resp.json()
        return {"answer": resp_data.get("answer", "调用Dify失败")}
    except Exception as e:
       return {"answer": resp_data.get("answer", f"调用Dify失败，Dify原始返回内容：{resp_data}")}
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)