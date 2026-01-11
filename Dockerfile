FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY src/ src/

# Copy models from repo
COPY models/ models/

# Verify models exist
RUN ls -lah models/ && \
    test -f models/model.pkl && \
    test -f models/scaler.pkl && \
    echo "✓ Models verified"

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]