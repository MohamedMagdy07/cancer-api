
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()
model = load('Colon_cancer_svc.joblib')


@app.get("/")
async def root():
    return {"message": "Hello World"}    
    

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
