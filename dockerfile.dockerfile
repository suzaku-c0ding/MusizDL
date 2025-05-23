FROM python:3.10-slim

WORKDIR /app

RUN pip install spotdl flask

COPY server.py .

CMD ["python", "server.py"]
