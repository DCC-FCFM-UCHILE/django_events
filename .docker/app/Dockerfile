FROM python:3.12-bookworm AS production

RUN mkdir -p /static /logs /media /backup /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
COPY app/ .
RUN pip install --upgrade pip
RUN pip install -r _requirements/base.txt -r _requirements/production.txt
RUN adduser -u 5678 --disabled-password --gecos "" instalar && chown -R instalar /static /logs /media /backup /app
USER instalar

FROM production AS develop

USER root
RUN apt-get update
RUN apt-get -y install --no-install-recommends graphviz graphviz-dev
RUN pip install -r _requirements/develop.txt
ENV PYDEVD_DISABLE_FILE_VALIDATION=1
# USER instalar
