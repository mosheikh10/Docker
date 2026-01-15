FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt . 
EXPOSE 5000

RUN pip install -r requirements.txt
COPY flaskapp.py .

CMD ["python", "flaskapp.py"]

