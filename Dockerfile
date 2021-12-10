FROM python:3.7-slim-buster
WORKDIR /opt/back-end
RUN mkdir -p /opt/back-end

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libffi-dev \
        libssl-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/back-end/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /opt/back-end

EXPOSE 8000
RUN python /opt/back-end/main.py