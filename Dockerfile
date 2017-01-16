##########################
##      contentkb-api   ##
##      Dockerfile      ##
##########################
FROM python:3.5-onbuild
# Add Phusion ppa
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
RUN apt-get update && \
    apt-get install -y \
        apt-transport-https \
        ca-certificates
RUN sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie main > /etc/apt/sources.list.d/passenger.list'

RUN apt-get update && \
    apt-get install -y \
        python-psycopg2 \
        passenger

EXPOSE 8000
CMD ["python", "./run.py"]