FROM python:3
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir resttest
ADD app.py .
ADD resttest/*.py resttest/
CMD python /app/app.py
