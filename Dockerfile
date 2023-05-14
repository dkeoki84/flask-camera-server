# Use image container
FROM ubuntu:20.04

# Set environments
ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

# Init container programs
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopencv-dev \
    python3-opencv \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set container workspace
WORKDIR /usr/src/app

# Copy app files
COPY ./templates ./templates
COPY app.py ./
COPY requirements.txt ./

# Update pip
RUN pip3 install --upgrade pip

# Install app requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Set entrypoint
ENTRYPOINT [ "python3" ]

# Set cmd
CMD [ "app.py" ]
