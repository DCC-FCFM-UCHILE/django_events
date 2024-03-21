FROM python:3.12.2-bookworm as production

ARG UID
ARG GID

RUN groupadd -r instalar
RUN useradd -m instalar -u ${UID} -g ${GID} -s /sbin/nologin
RUN mkdir -p /static /logs /media /backup /home/instalar/app
RUN chown -R instalar:instalar /static /logs /media /backup /home/instalar/app

USER instalar
WORKDIR /home/instalar/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/instalar/.local/bin:${PATH}"

COPY --chown=instalar:instalar app/ .

RUN pip install --upgrade pip
RUN pip install -r _requirements/base.txt -r _requirements/production.txt


FROM production as develop

USER root
RUN apt-get update
RUN apt-get -y install --no-install-recommends graphviz graphviz-dev 

USER instalar
RUN pip install -r _requirements/develop.txt
