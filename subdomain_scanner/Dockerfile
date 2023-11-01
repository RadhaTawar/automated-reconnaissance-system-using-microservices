FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4017

ENV NAME Subdomain_Scanner

CMD python app.py
