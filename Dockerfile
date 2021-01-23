FROM python:3.8.7-slim

WORKDIR /code
COPY requirements.txt requirements.txt

RUN pip install -U pip \
    && pip install --no-cache-dir -r /code/requirements.txt

COPY . .

ENTRYPOINT ["python", "lang_simplification.py"]
