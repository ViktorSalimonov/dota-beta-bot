FROM python:3.10.9-alpine

RUN apk update

WORKDIR /code

COPY requirements.txt code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r code/requirements.txt

COPY . /code/app

CMD ["python", "app/bot.py"]
