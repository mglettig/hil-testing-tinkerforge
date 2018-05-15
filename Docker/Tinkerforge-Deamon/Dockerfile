# Note: The device /dev/bus/usb needs to be mounted from host to docker container.

FROM ubuntu:16.04

MAINTAINER remo.buechele@zuehlke.com

RUN apt-get update

# Install Brick Daemon

RUN apt-get update && apt-get install -y --no-install-recommends \
	pkg-config \
	libusb-1.0-0-dev \
	libudev-dev \
	wget \
	pm-utils \
	&& rm -rf /var/lib/apt/lists/*

RUN wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb \
	&& dpkg -i brickd_linux_latest_amd64.deb

WORKDIR /work

# Provide port of Brick Daemon for other containers
EXPOSE 4223

# ENTRYPOINT ["/bin/bash"]
CMD /etc/init.d/brickd start && tail -f /dev/null

#RUN /etc/init.d/brickd force-reload
