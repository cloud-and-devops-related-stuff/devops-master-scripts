# AWS EC2 Docker Deployment Via SSM Agent

This script refreshes running docker images inside an EC2 Server Via SSM Agent.

## Assumtions:

- EC2 Instance is up and running.
- SSM Agent is available in EC2 Instance.
- EC2 Instance have required permissions for being managed by System Manager.
- docker-compose.yml file is present at the known location.


## Working:

Run below commands inside the image:

- export aws_access_key_id=${aws_access_key_id}
- export aws_secret_access_key=${aws_secret_access_key}
- export region_name=${region_name}
- export aws_instance_id=${aws_instance_id}
- export artifactory_url=${artifactory_url}
- export artifactory_username=${artifactory_username}
- export artifactory_password=${artifactory_password}
- python /home/devops/aws-ssm-ec2-docker-deploy/main.py

In above steps, setting environment variables steps can be ignored if they already available.


## Contribution:

All the suggestions & contributions are appreciated and most welcomed. Thanks