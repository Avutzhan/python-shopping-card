FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD FLASK_APP=app.py FLASK_DEBUG=1 flask run --host=0.0.0.0