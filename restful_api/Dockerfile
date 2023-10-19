FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	python3.10 \
	python3.10-dev \
	python3-pip

RUN pip3 install \
	fastapi \
	"uvicorn[standard]" \
	mysql-connector-python \
	requests

ENV RESTFUL_API_HOME=/home/restful_api

WORKDIR ${RESTFUL_API_HOME}

ENV PYTHONPATH=${RESTFUL_API_HOME}
ENV PYTHONPATH=${RESTFUL_API_HOME}/core:${RESTFUL_API_HOME}

COPY core /home/restful_api/core

COPY models /home/restful_api/models

CMD ["python3", "core/run.py"]
