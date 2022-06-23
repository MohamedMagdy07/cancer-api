
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'fuck you'}    
    
    
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
