import boto3

ec2_client = boto3.client('ec2', region_name='us-west-2')
ec2_list = ec2_client.describe_instances(Filters=[{'Name': 'tag:Environment','Values': ['dev']},{'Name':'instance-state-name', 'Values': ['stopped']}])
#print (ec2_list)
if not ec2_list:
    print ("Required Target Instances are in Running State")

else:
    for ec2 in ec2_list['Reservations']:
        for ec2_instance in ec2['Instances']:
            print(f"ALERT --> {ec2_instance['InstanceId']} is not running")