#Step 1: 
# Search --> Command Prompt-->open
# python -m venv neetu
# neetu\Scripts\activate
# cd neetu
# pip install wandb
# wandb login –relogin (this if u r login again)  wandb login (this if u r login for first time)
# go to chrome --> https://wandb.ai/authorize  --> login
# Copy  API key  46163da69bb968495c441082fe01e98c3281f146
# Go back to cmd --> pip install scikit-learn
# Go to IDLE -->
import wandb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

wandb.init(project="ml-project", name="gridsearch_example")
data = load_iris()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

rf = RandomForestClassifier()
grid = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)

wandb.config.update({"model": "RandomForest", "param_grid": str(param_grid)})

grid.fit(x_train, y_train)

wandb.config.update({
    "best_n_estimators": grid.best_params_['n_estimators'],
    "best_max_depth": grid.best_params_['max_depth']
})

y_pred = grid.best_estimator_.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

wandb.log({"accuracy": accuracy}) 

#save the idle file in the folder u create



# go to cmd
# python neetu.py 
# after running the above code u will get the link code the go chrome --> to see the output

import wandb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

wandb.init(project="ml-project", name="gridsearch_example")

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define parameter grid
param_grid = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

# Random Forest classifier with GridSearchCV
rf = RandomForestClassifier()
grid = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1)

# Fit the model
grid.fit(X_train, y_train)

# Log best parameters
wandb.config.update({
    "model": "RandomForest",
    "param_grid": str(param_grid),
    "best_n_estimators": grid.best_params_['n_estimators'],
    "best_max_depth": grid.best_params_['max_depth']
})

# Predict and log metrics
y_pred = grid.best_estimator_.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

wandb.log({
    "accuracy": accuracy,
    "mse": mse,
    "mae": mae,
    "r2": r2
})
#save the idle file in the folder u create
# go to cmd
# python neetu.py 
# after running the above code u will get the link code the go chrome --> to see the output
