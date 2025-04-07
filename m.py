#Download python 3.10.1
#python 3.10.1 --> click on Download --> Windows installer (64-bit)
#Setup -->tick on add python 3.10 to Path -->click on install now
# cmd
#  python –version
# python -m venv rohan
# rohan\Scripts\activate
# pip install mlflow numpy scikit-learn
# cd rohan 
# mkdri run_mlflow
# cd run_mlflow
# python pract.py
# mlflow ui

# save this --> pract.py 
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
x=np.array([[1],[2],[5],[9],[6],[3],[4],[7],[8]])
y=np.array([1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9])
mlflow.set_experiment("information")
with mlflow.start_run():
    model=LinearRegression()
    model.fit(x,y)
    y_p=model.predict(x)
    mse=mean_squared_error(y,y_p)
    mae=mean_absolute_error(y,y_p)
    mlflow.log_param("intercept",model.fit_intercept)
    mlflow.log_param("feature",x.shape[1])
    mlflow.log_param("sample",x.shape[0])
    mlflow.log_metric("mse",mse)
    mlflow.log_metric("mae",mae)
    mlflow.sklearn.log_model(model,"model")
print("log done run ui and check")


# localhost:5000

