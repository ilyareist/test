import logging, boto3, time

# import time
# import requests
# from createEC2 import create_ec2
# # from .createECSService import *
# # from .createTaskDefinition import createTaskDefinition
# # from .elbv2Services import *
# # from .createECSCluster import createECSCluster
from resources import *
# from pprint import pprint
# # creating
# print('Creating EC2 instances...')
# # instances = create_ec2(ec2_client)["Instances"]
# # instanceID=instances[0]["InstanceId"]
# # pprint(instanceID)
#
# waiter=ec2_client.get_waiter('instance_running')
# print(waiter.wait(InstanceIds=["i-051c3f5ef60db25b9"]))


boto3.set_stream_logger('boto3', logging.DEBUG)
ec2 = ec2_resource
instance = ec2.create_instances(
    ImageId='ami-64300001',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
)[0]
print('Created instance:', instance.id)
instance.wait_until_running()
time.sleep(5)
instance.terminate()
instance.wait_until_terminated()
print('Terminated instance:', instance.id)