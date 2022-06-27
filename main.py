
from fastapi import FastAPI, Body,UploadFile,Header,File,HTTPException
from joblib import load
import pandas as pd
import sys
import os

app = FastAPI(debug=True)

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    print(base_path)
    return os.path.join(base_path, relative_path)


model = load(resource_path('Colon_cancer_svc.joblib'))    


@app.post("/")
async def root():
    return {"message": 'Hello'}    
    

@app.post("/uploadcsv/",)
async def upload_file(file: UploadFile = File(...)):
    
    data = pd.read_csv(file.file, header=None)
    if len(data.columns) == 50:
        prediction =pd.Series(model.predict(data))
        print(prediction)
        result = pd.DataFrame(prediction)
        print(result)
        result = result.replace({0: 'Normal', 1: 'Tumoral '})
        result = result[0].iloc[0]
    else:
        result = "Please Upload Usable Data File"
    return {"prediction": result,}    

