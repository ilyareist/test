import logging, boto3, time

# import time
# import requests
# from createEC2 import create_ec2
# # from .createECSService import *
# # from .createTaskDefinition import createTaskDefinition
# # from .elbv2Services import *
# # from .createECSCluster import createECSCluster
from resources import *
from pprint import pprint


boto3.set_stream_logger('boto3', logging.DEBUG)
ec2 = ec2_resource
instance = ec2.create_instances(
    ImageId='ami-64300001',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    IamInstanceProfile={
            "Name": "ecsInstanceRole"
        },
    SecurityGroups=[
        'default',
    ],
    KeyName='aws_new',
)[0]
instance.wait_until_running()
instance.reload()

print(instance.public_dns_name)
print(instance.public_ip_address)
print(instance.state)



# ecs_client = boto3.client(
#     'ecs',
#     aws_access_key_id=access_key,
#     aws_secret_access_key=secret_key,
#     region_name=region
# )
#
# response = ecs_client.register_task_definition(
#     containerDefinitions=[
#         {
#           "name": "nginx",
#           "image": "890520118857.dkr.ecr.us-east-2.amazonaws.com/test:latest",
#           "entryPoint": [
#             "/deployment/env/bin/python",
#             "/deployment/start.py"
#           ],
#           "command": [""],
#           "environment": [],
#           "mountPoints": [],
#           "volumesFrom": [],
#           "logConfiguration": {
#             "logDriver": "awslogs",
#             "options": {
#                 "awslogs-group": "awslogs-flask",
#                 "awslogs-region": "us-east-2",
#                 "awslogs-stream-prefix": "awslogs-flask"
#             }
#           },
#           "portMappings": [
#             {
#               "containerPort": 5000,
#               "hostPort": 5000
#             }
#           ],
#           "memory": 256,
#           "cpu": 512
#         }
#     ],
#     family="flask"
# )




response = ecs_client.create_service(
    cluster="default",
    serviceName="ECR",
    taskDefinition="flask",
    desiredCount=1,
    clientToken='request_identifier_string',
    deploymentConfiguration={
        'maximumPercent': 200,
        'minimumHealthyPercent': 50
    },
)
print(response)


