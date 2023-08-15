FROM ubuntu:22.04

# Installing openssh-client, Python & PIP3
RUN apt-get update && apt-get -y upgrade && apt-get install python3 python3-pip  -y
RUN pip3 --version
RUN pip3 install --no-cache-dir awscli boto3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Define working directory.
WORKDIR /home/devops

# Copy Files
COPY . ./

# Define default command.
CMD ["bash"]