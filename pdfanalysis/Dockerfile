FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4013

ENV NAME pdfanalysis

CMD python app.py
