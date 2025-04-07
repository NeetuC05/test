!pip install scikit-learn

from sklearn.datasets import load_wine
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = load_wine()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=20)
model = SVC()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy:{accuracy:.4f}")


from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_squared_error
data = load_iris()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=20)
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy:{accuracy:.4f}")
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error:{mse:.4f}")
