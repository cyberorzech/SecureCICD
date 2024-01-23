FROM python:3.10
WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python3.10", "-m", "uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]