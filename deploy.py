import time
import requests
from .createEC2 import create_ec2
# from .createECSService import *
# from .createTaskDefinition import createTaskDefinition
# from .elbv2Services import *
# from .createECSCluster import createECSCluster
from .resources import *


# creating EC2 instances
print('Creating EC2 instances...')
instances = create_ec2(ec2_client)["Instances"]