import sys
import time

from ssm_helper import execute_command, get_command_status
from commons import aws_instance_id, artifactory_url, artifactory_username, artifactory_password

# Configure logging
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


# Run Pipeline Commands.
def main():
    
    logging.info("Starting Command Execution")

    logging.info("Configuring Commands To Be Sent")

    docker_login_cmd = f'echo {artifactory_password} | docker login -u {artifactory_username} --password-stdin {artifactory_url}'
    commands = [
        docker_login_cmd,
        'docker compose pull',
        'docker compose up -d',
        'docker image prune -a -f',
        f'docker logout {artifactory_url}'
    ]


    logging.info("Commands Configured Successfully")


    command_id= execute_command(commands, aws_instance_id)

    logging.info("Command Id Retrieved Successfully")

    attempts=0

    while True:

        attempts+=1

        logging.info(f"Performing Command Status Check With Attempt: {attempts}")

        time.sleep(10)

        command_state = get_command_status(command_id, aws_instance_id)

        command_status = command_state['Status']


        if command_status in ['Cancelled','TimedOut','Failed','Cancelling']:
            logging.error("Command Invocation Failed.")
            logging.error("----------------------------------------------------------")
            logging.error(f"Standard Output: {command_state['StandardOutputContent']}")
            logging.error("----------------------------------------------------------")
            logging.error(f"Standard Error: {command_state['StandardErrorContent']}")
            logging.error("----------------------------------------------------------")
            sys.exit(1)

        elif command_status in ['Pending','InProgress','Delayed']:
            logging.info("Command Is INP Status")
        elif command_status == 'Success':
            logging.info("Command Invocation Successful.")
            logging.info("----------------------------------------------------------")
            logging.error(f"Standard Output: {command_state['StandardOutputContent']}")
            logging.info("----------------------------------------------------------")
            sys.exit(0)
        else:
            logging.error(f"Command status '{command_status}' processing is not defined. Treating as failure.")
            sys.exit(1)


if __name__ == "__main__":
    main()