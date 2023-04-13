# Filename: Dockerfile 

FROM python:3.6
MAINTAINER XenonStack
 
# Creating Application Source Code Directory
RUN mkdir -p /web-app

# Setting Home Directory for containers
WORKDIR /web-app

# Installing python dependencies
COPY /web-app/requirements.txt /web-app/
RUN pip install -r requirements.txt

# Copying src code to Container
COPY /web-app/. /web-app/

# Application Environment variables
ENV APP_ENV development
# Exposing Ports
EXPOSE 5000
# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD ["python3", "app.py"]