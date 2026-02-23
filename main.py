from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running locally!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    # Run with uvicorn, binding to localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)