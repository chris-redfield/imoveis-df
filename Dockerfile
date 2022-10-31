FROM python:3.7-alpine 

RUN apk add gcc libev-dev musl-dev

ENV ENV=${ENV}
ENV PORT=${PORT}
ENV HOST=${HOST}

WORKDIR /code

ADD requirements.txt /code 
RUN pip install -r requirements.txt
ADD . /code

EXPOSE 5000
CMD ["python", "api/app_server.py"]