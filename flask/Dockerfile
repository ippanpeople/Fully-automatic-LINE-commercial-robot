FROM python:3.7.15

WORKDIR /app

ADD . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary 

CMD ["python3", "app.py"] 
