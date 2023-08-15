FROM ubuntu:23.10

# Installing openssh-client, Python & PIP3
RUN apt-get update && apt-get -y upgrade && apt-get install openssh-client python3 python3-pip  -y
RUN pip3 --version
RUN pip3 install awscli
RUN pip3 install boto3

# Define working directory.
WORKDIR /home/devops

# Copy Files
COPY . ./

# Define default command.
CMD ["bash"]