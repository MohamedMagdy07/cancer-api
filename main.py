
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd
import sys
import os

app = FastAPI()

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    print(base_path)
    return os.path.join(base_path, relative_path)


@app.post("/")
async def root():
    model = load(resource_path('Colon_cancer_svc.joblib'))    
    return {"message": 'hello'}    
    
#@app.on_event('startup')
#def load_model():
    
    
    
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
