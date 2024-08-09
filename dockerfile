# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /a
RUN pwd
# install dependencies
RUN pip install --upgrade pip
COPY keras_model.h5 .
# copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install tensorflow==2.10.0
#RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .
RUN pwd
RUN pip list
# command to run on container start
#CMD [ "python3 ", "--version"]
CMD [ "python3", "main.py" ]