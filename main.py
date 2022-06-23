
from fastapi import FastAPI, Body,UploadFile,Header,File
import pandas as pd
from joblib import load

Model = load('Colon_cancer_svc.joblib')


app = FastAPI()



@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}


@app.on_event('startup')
def load_model():
    global model
    model = Model



@app.post("/uploadcsv")
async def upload_file(file: UploadFile):
    dataframe = pd.read_csv(file.file)
    prediction = model.predict(dataframe).tolist()
    result=pd.DataFrame(prediction)
    result=result.replace({0:'normal',1:'adenocarcinoma'})
    result=result.values.tolist()
    return {"prediction": result,}    
    
