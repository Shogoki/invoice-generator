FROM python:3.7-slim

WORKDIR /usr/src/app
RUN apt-get update && apt-get install wkhtmltopdf -y
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app

CMD ["python3", "-m", "backend"]