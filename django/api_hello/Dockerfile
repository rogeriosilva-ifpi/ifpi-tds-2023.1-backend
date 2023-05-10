FROM bitnami/python:3.11.2
WORKDIR /app

COPY . .

# COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", '--reload']
# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", '--reload']
