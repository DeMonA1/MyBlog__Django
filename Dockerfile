FROM python:3.12

RUN apt-get update -qq \
    && rm -rf /var/lib/apt/lists/*

# set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install psycopg[binary]

COPY . .