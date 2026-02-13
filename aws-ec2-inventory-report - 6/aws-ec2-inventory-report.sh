#!/bin/bash

## Fetch Input

#region_list=$(aws ec2 describe-regions --query 'Regions[].RegionName' --output text)
#echo -e "$region_list\\n"
read -p $'Enter the aws region to generate the inventory list:\n' region

if [ -z "$region" ]; then
   echo -e "Empty Inputs provided, Provide AWS region\\n"
   exit
else
   if echo "$(aws ec2 describe-regions --query 'Regions[].RegionName' --output text)" | grep -qw "$region"; then ## provides output as a string instead of list
      echo -e "Valid AWS Region\\n"
   else
      echo "Invalid AWS Region"
      exit
   fi
fi

echo -e "*************** GENERATING EC2 INVENTORY REPORT **************\\n"

aws ec2 describe-instances --query "Reservations[*].Instances[*].{Id:InstanceId,State:State.Name,InstanceType:InstanceType,AZ:Placement.AvailabilityZone,PublicIpAddress:PublicIpAddress}" --output text | whileread az instance_id instance_type public_ip instance_state; do
    echo -e "Instance ID: $instance_id\\n"
    echo -e "Instance TYPE: $instance_type\\n"
    echo -e "Instance STATE: $instance_state\\n"
    echo -e "Instance AZ: $az\\n"
    echo -e "Instance PUBLIC IP: $public_ip\\n"
    echo -e "============================================================\\n"
done

echo -e "*************** END OF EC2 INVENTORY REPORT **************"