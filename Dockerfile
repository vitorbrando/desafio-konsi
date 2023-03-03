FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache pkgconfig \
                       gcc \
                       libc-dev \
                       cmake \
                       chromium \
                       chromium-chromedriver \
                       unzip \
    && rm -rf /var/cache/apk/*

RUN pip3 install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["main.py" ]