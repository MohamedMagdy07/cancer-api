
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}    

@app.on_event('startup')
async def load_model():
    model = load('Colon_cancer_svc.joblib')
    
    
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
