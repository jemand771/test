FROM python:3

WORKDIR /app
COPY *.py .

CMD ["python3", "hello.py"]