FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4023

ENV NAME ipdomains

CMD python app.py
