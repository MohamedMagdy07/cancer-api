
from fastapi import FastAPI, Body,UploadFile,Header,File
from joblib import load
import pandas as pd

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.on_event('startup')
def load_model():
    global model
    model = load('Colon_cancer_svc.joblib')



@app.post("/uploadcsv")
async def upload_file(file: UploadFile):
    dataframe = pd.read_csv(file.file)
    prediction = model.predict(dataframe).tolist()
    result=pd.DataFrame(prediction)
    result=result.replace({0:'normal',1:'adenocarcinoma'})
    result=result.values.tolist()
    return {"prediction": result,}    
    
