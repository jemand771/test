FROM python:3.12-slim

WORKDIR /app
COPY *.py .

CMD ["python3", "hello.py"]
