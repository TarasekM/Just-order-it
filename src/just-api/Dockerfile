FROM python:3.7-buster

COPY requirements.txt /just-api/
COPY just_api /just-api/just_api
COPY wsgi.py /just-api/
# COPY tests /just-api/
COPY cmd.sh /just-api/

WORKDIR /just-api/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pip install uWSGI pytest

ENV FLASK_RUN_PORT=9000
EXPOSE ${FLASK_RUN_PORT}

RUN groupadd -r just-api && useradd -r -g just-api just-api
RUN chown -R just-api:just-api /just-api
USER just-api

CMD ["sh", "/just-api/cmd.sh"]
