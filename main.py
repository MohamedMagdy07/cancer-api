
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()


@app.post("/")
async def root():
    model = load('./Colon_cancer_svc.joblib')
    return {"message": model}    
    
    
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
