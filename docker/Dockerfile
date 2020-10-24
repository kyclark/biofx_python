FROM python:3.8.3-buster
RUN apt-get -y update
RUN apt-get install -y git vim emacs

WORKDIR /app
RUN git clone https://github.com/kyclark/biofx_python && python3 -m pip install -r /app/biofx_python/requirements.txt

RUN cp /app/biofx_python/.mypy.ini ~
RUN cp /app/biofx_python/.pylintrc ~

CMD ["python3", "--version"]
