FROM python:3.6

MAINTAINER darrell.cox

COPY . /app
WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

EXPOSE 8000

ENV http_proxy cache2.uk.logica.com:80
ENV https_proxy cache2.uk.logica.com:80

CMD ["python", "run.py"]