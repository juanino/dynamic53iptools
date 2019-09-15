#!/usr/bin/python3


# this utility is used tell SQS a machine booted or otherwise changed
# so a control box can process a hostname change or other functions

import boto3
import sys
from time import sleep
import pprint
import time

epoch_time = str(time.time())
try:
    queue_name = sys.argv[1]
    ip = sys.argv[2]
except:
    print("Usage: ./sqs_send_event.py [queue name] [event] ")
    sys.exit(2)

# we will use the queue passed
q_name = queue_name
print("using queue name " + q_name)

# get the service resource
sqs = boto3.resource('sqs')

# fetch that queue resource
inject_q = sqs.get_queue_by_name(QueueName=q_name)

response = inject_q.send_message(MessageBody=ip,MessageGroupId="send_ip.py",MessageDeduplicationId=epoch_time)
pprint.pprint(response)
print("tx: " + str(ip))