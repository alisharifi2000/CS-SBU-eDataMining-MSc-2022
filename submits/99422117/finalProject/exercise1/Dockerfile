FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

ENTRYPOINT ["python"]

CMD ["app.py"]