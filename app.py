import os
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import List, Optional
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

API_TOKEN = os.getenv("API_TOKEN")

class TextRequest(BaseModel):
    texts: List[str]

def verify_token(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ")[1]
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.post("/embed")
def embed(request: TextRequest, _: None = Depends(verify_token)):
    vectors = model.encode(request.texts, convert_to_tensor=False)
    return {"embeddings": [v.tolist() for v in vectors]}

@app.get("/warmup")
def warmup(_: None = Depends(verify_token)):
    try:
        _ = model.encode(["warmup"], convert_to_tensor=False)
        return {"status": "Model warmed up"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Warmup failed: {str(e)}")



# import os
# from fastapi import FastAPI, HTTPException, Header, Depends
# from pydantic import BaseModel
# from typing import List, Optional
# from sentence_transformers import SentenceTransformer

# app = FastAPI()
# model = SentenceTransformer("all-MiniLM-L6-v2")

# API_TOKEN = os.getenv("API_TOKEN")

# class TextRequest(BaseModel):
#     texts: List[str]

# def verify_token(authorization: Optional[str] = Header(None)):
#     if authorization is None or not authorization.startswith("Bearer "):
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     token = authorization.split(" ")[1]
#     if token != API_TOKEN:
#         raise HTTPException(status_code=403, detail="Invalid token")

# @app.post("/embed")
# def embed(request: TextRequest, _: None = Depends(verify_token)):
#     vectors = model.encode(request.texts, convert_to_tensor=False)
#     return {"embeddings": [v.tolist() for v in vectors]}
