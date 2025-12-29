# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app
ENV FASTAPI_APP=run.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]