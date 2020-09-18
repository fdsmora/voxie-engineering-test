FROM ubuntu:latest
MAINTAINER Fausto Mora "fausto.ds.mora@gmail.com"
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    curl
ENV FLASK_APP=project
ENV FLASK_ENV=development
COPY . /voxie-engineering-test
WORKDIR /voxie-engineering-test
RUN pip3 install -r /voxie-engineering-test/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "/voxie-engineering-test/run_this_app.sh" ]
