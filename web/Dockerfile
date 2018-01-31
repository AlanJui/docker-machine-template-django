FROM python:3.6.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# copies everything in current directory into filesystem of image in /code/ directory.
#COPY . /code/
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt

ADD ./ /code/

