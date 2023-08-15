import os

# Configure logging
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Fetch variables from environment
aws_access_key_id = os.environ.get('aws_access_key_id')
aws_secret_access_key = os.environ.get('aws_secret_access_key')
region_name= os.environ.get('region_name')
aws_instance_id= os.environ.get('aws_instance_id')
artifactory_url= os.environ.get('artifactory_url')
artifactory_username= os.environ.get('artifactory_username')
artifactory_password= os.environ.get('artifactory_password')

# Check if any of the environment variables are missing
missing_variables = []
if aws_access_key_id is None:
    missing_variables.append('aws_access_key_id')
if aws_secret_access_key is None:
    missing_variables.append('aws_secret_access_key')
if region_name is None:
    missing_variables.append('region_name')
if aws_instance_id is None:
    missing_variables.append('aws_instance_id')
if artifactory_url is None:
    missing_variables.append('artifactory_url')
if artifactory_username is None:
    missing_variables.append('artifactory_username')
if artifactory_password is None:
    missing_variables.append('artifactory_password')


# If there are missing variables, print them and raise an exception
if missing_variables:
    logging.error("Missing environment variables:", ', '.join(missing_variables))
    raise Exception("One or more required environment variables are missing")


# Export the variables for other scripts to use
__all__ = ["aws_access_key_id", "aws_secret_access_key", "region_name", "aws_instance_id", "artifactory_url", "artifactory_username", "artifactory_password"]
