import boto3
from commons import aws_access_key_id, aws_secret_access_key, region_name

# Configure logging
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Method to send Docker Image Refresh Command to EC2 Instances
def execute_command(commands, instance_id):

    logging.info("Creating SSM Client")
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    ssm_client = session.client('ssm')

    logging.info("SSM Client Created Successfully")

    logging.info("Sending SSM Command")
    
    send_command_response = ssm_client.send_command(
        InstanceIds=[instance_id],
        DocumentName="AWS-RunShellScript",
        Comment="Refresh Docker Images From Pipeline",
        Parameters={
            'commands': commands,
            'workingDirectory': ['/home/ubuntu']
        }
    )

    command_id = send_command_response['Command']['CommandId']
    logging.info(f"Command Sent Successfully With Command ID: {command_id}")
    
    return command_id


# Method to Get Command Status From AWS SSM Command ID
def get_command_status(command_id, instance_id):

    logging.info("Creating SSM Client")
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    ssm_client = session.client('ssm')
    logging.info("SSM Client Created Successfully")

    logging.info(f"Fetching the Command Status For Command ID: {command_id}")

    response = ssm_client.get_command_invocation(
            CommandId=command_id,
            InstanceId=instance_id
    )

    logging.info(f"Command Status Fetched Successfully As: {response['Status']}")

    return response