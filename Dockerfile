FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Pull data + models from DVC remote
RUN dvc pull

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
