##########################
##      contentkb-api   ##
##      Dockerfile      ##
##########################
FROM debian:jessie

# Add Phusion ppa
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
RUN apt-get update && \
    apt-get install -y \
        apt-transport-https \
        ca-certificates
RUN sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie main > /etc/apt/sources.list.d/passenger.list'

RUN apt-get update && \
    apt-get install -y \
        nginx-extras

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]