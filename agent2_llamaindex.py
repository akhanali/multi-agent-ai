import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import uvicorn

# Load PDF
docs = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()

app = FastAPI()

@app.post("/a2a")
async def receive_message(request: Request):
    data = await request.json()
    query = data["content"]
    result = query_engine.query(query)
    return {"response": str(result)}

if __name__ == "__main__":
    uvicorn.run("agent2_llamaindex:app", host="127.0.0.1", port=8000)
