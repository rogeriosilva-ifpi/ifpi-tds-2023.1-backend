FROM bitnami/python:3.11.2
WORKDIR /app

COPY . /app

# COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", '--reload']
# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", '--reload']
