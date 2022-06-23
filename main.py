
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}    
    
@app.get("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.get("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
