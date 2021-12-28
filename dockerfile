FROM python:3
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
LABEL maintainer johnkischel@gmail.com
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
