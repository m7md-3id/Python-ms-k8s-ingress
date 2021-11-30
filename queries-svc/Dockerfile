FROM python:3.9-alpine

WORKDIR /tmp/app

COPY . /tmp/app/

RUN pip install -r requierments.txt

EXPOSE 82

CMD python q-app.py
