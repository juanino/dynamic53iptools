#!/bin/bash

# replace i- number with the instance you want to watch for changes to ip
IP=`aws ec2 describe-instances --instance-id i-XXXXXXXXXXXXXXXXX --output text --query 'Reservations[].Instances[].PublicIpAddress'`

echo "instance is found running ${IP}"

# template should exist
# but change.json is created
cat template.json  | sed "s/XXXX/${IP}/g" > change.json

# hosted-zone-id can be obtained from the route53 console
aws route53 change-resource-record-sets --hosted-zone-id XXXXXXXXXXXXXX --change-batch file://change.json

# when you are done with changes this should be called fetch_set_dns.sh
