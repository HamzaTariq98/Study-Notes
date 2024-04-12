FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

RUN pip install gunicorn

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
