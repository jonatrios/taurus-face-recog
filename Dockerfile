FROM python:3.8

#Set the working directory
WORKDIR /

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 5000

ENV python-3.8.10
#Run the command
CMD gunicorn main:app