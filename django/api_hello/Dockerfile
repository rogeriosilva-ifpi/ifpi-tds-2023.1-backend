FROM bitnami/python:3.11.2
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
