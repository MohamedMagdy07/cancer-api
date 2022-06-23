
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


model = load(resource_path('Colon_cancer_svc.joblib'))    


@app.post("/")
async def root():
    return {"message": 'Hello'}    
    

@app.post("/uploadcsv")
async def upload_file(file: UploadFile):
    dataframe = pd.read_csv(file.file, header=None)
    prediction = model.predict(dataframe).tolist()
    print(prediction)
    result=pd.DataFrame(prediction)
    result=result.replace({0:'Normal',1:'Tomural'})
    result=result.values.tolist()
    return {"result": result,"prediction":prediction.tolist()}   
