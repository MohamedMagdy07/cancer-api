
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
    return {"message": model}    
    

@app.post("/uploadcsv")
async def upload_file(file: UploadFile):
    data = pd.read_csv(file.file, header=None)
    if len(data.columns) == 50:
        prediction = model.predict(data).tolist()
        if prediction==0 :
            result='normal'
        elif prediction==1:
            result='tomural'
        result=pd.DataFrame(result)
    else:
        result = "Please Upload Usable Data File"
    return {"prediction": result,}   
