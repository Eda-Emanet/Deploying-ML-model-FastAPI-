from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
# Uygulama oluştur
app = FastAPI(title="Churn Prediction API")

# Modeli yükle
model = joblib.load("xgb_model.pkl")

# Kullanıcıdan alınacak veri formatı
class CustomerFeatures(BaseModel):
    creditscore: int 
    age: int
    tenure : int 
    balance: float
    numofproducts: int
    isactivemember: int
    estimatedsalary: float
    

@app.get("/")
def root():
    return {"message": "Churn Prediction API çalışıyor"}


@app.post("/predict")
def predict_churn(data: CustomerFeatures):
    input_data = np.array([[data.creditscore, data.age, data.tenure, data.balance,
                            data.numofproducts, data.isactivemember,
                            data.estimatedsalary]])
    prediction = model.predict(input_data)
    return {"churn_prediction": int(prediction[0])}

 
@app.get("/test")
def test():
    return {"message": "Test başarılı"}

##uvicorn main:app --reload # çalıştırmak için  terminale yaz
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

