FROM python:3.6.9
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt install python3-dev -y
RUN apt install build-essential -y
RUN pip install --upgrade pip setuptools
COPY requirements.txt /usr/
RUN pip install -r /usr/requirements.txt
EXPOSE 5000