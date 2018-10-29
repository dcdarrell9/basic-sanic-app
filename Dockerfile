FROM python:3.7

MAINTAINER darrell.cox

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

EXPOSE 8000

ENV http_proxy cache2.uk.logica.com:80
ENV https_proxy cache2.uk.logica.com:80

CMD ["python", "run.py"]