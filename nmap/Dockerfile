FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y sudo

RUN useradd -ms /bin/bash nmapuser && echo "nmapuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER nmapuser

RUN sudo pip install --no-cache-dir -r requirements.txt

EXPOSE 4020

ENV NAME SQL_Injection

CMD python app.py
