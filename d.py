# wsl --unregister Ubuntu
# wsl --install -d Ubuntu
#d:
# go to file --> Local Disk ( D: ) --> create a new folder by your name (eg ML)
# App.py --> create this file on “IDLE” --> in that write -->  print(“hello world”) --> save the in Local Disk ( D: ) then go   select the ML folder save in the as aap.py
# requirements.txt --> create this file on “Notepad” --> in that write --> 
flask
numpy
pillow
# Dockerfile --> create this file on “Notepad” --> in that write -->
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --ni-cache-dir -r requirements.txt
CMD ["python", "app.py"]

# cmd-->
# cd ML
# docker build -t python-app .
# ( if the Dokerfile is a text file not all file --> then this error can come to solve it  --> Step to solve the error  dir D:\ML  --> ren Dockerfile.txt Dockerfile --> docker build -t python-app . )
# to see the output -->  docker run --name ML python-app
# to stop the output --> docker rm ML
