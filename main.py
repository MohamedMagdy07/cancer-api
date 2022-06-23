
from fastapi import FastAPI

app = FastAPI(title="Colon ML API", description="Colon for iris dataset ml model", version="1.0",)

@app.get("/")
async def root():
    return {"message": "Hello World"}
