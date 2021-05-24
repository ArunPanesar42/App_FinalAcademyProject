FROM python:3

WORKDIR /usr/src/app


RUN apt-get update -y
RUN apt-get install dos2unix -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY  ./ /usr/src/app

CMD [ "python",  "main.py"]