#Cmd -->
# FLASK
# pip install flask
# pip install joblib
# pip install gunicorn
# pip install numpy
# Go to IDLE and type ->
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def home():
    if request.method == 'GET':
        return "my first api"
    elif request.method == 'POST':
        return "hello there"
    elif request.method == 'PUT':
        return "Yokoso Minnachan!"

if __name__ == '__main__':
    app.run(debug=True)
# Now go to the location where this file is saved (save it to desktop)
# In Command prompt
# Cd Desktop
# Python filename.py ( python app_flask.py)
# The output will be as shown below
# python app_flask.py

# fastAPI
# pip install fastapi
# pip install unicorn uvicorn
# pip install joblib
# pip install numpy 
# Create a python file as shown (Preferably in desktop)
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
# Load the dataset
data = load_iris()
x = data.data
y = data.target
# Create and train the model
model = RandomForestClassifier(n_estimators=100)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model.fit(x_train, y_train)
# Save the model
joblib.dump(model, 'mymodel.pkl')
print("mymodel.pkl")

# Now again in cmd
# cd Desktop
# python filename.py ( python app_fast.py  )
# Your pkl file will be generated as shown below

# Now create a new python file as shown
from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np
# Load the model
model = joblib.load("mymodel.pkl")
# Create the FastAPI app
app = FastAPI()
@app.get("/")
def load_model():
    return "Hello model"

@app.post("/predict")
async def predict_model(request: Request):
    body = await request.json()
    data = body["data"]
    pred = model.predict([data])
    print(pred)
    return {"pred": int(pred[0])}

# Go to cmd and do the following
# uvicorn main:app --reload


