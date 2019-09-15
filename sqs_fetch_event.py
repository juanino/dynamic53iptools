#!/usr/bin/python3

# consume the queue 
# and set the ip pushed to us from the send_ip.py script

import boto3
import sys
from time import sleep
import os

# get queue to look for ip change requests, as first arg passed
# this should be the same as 
try:
    queue_name = sys.argv[1]
    print("I\'m going to look for work in " + queue_name)
except:
    print("Usage: ./sqs_fetch_event.py [queue name]")
    sys.exit(2)

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
work_q = sqs.get_queue_by_name(QueueName=queue_name)

# check the queue
while True:
    print("checking for work")
    # max is 20 seconds per docs
    for message in work_q.receive_messages(WaitTimeSeconds=20):
        print('rx: ' + message.body)
        if message.body == "booted":
            os.system("./fetch_set_dns.sh")
        message.delete()
    print("waiting 40 sec for next poll")
    sleep(40)
