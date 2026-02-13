import boto3
import datetime
from datetime import timezone
from botocore.exceptions import ClientError

region = input("Enter the AWS Region: ")
threshold_days = input("Enter the Threshold number of Days to filter the orphan EBS: ")
try:
    if not all([region,threshold_days]):
         print("Empty Inputs for AWS Region or Threshold days Provided... Please Check!")
         exit
    else:
        ec2_client = boto3.client('ec2', region_name=region)
        reg_response = ec2_client.describe_regions()
        #print(reg_response)
        regions = [reg['RegionName'] for reg in reg_response['Regions']]
        #print(regions)
        if region not in regions:
          print("Invalid AWS Region Input...Please Try Again")
          exit
        else:
          print("Valid AWS Region Input")
          volumes = ec2_client.describe_volumes(
          Filters=[
          {
            'Name': 'status',
            'Values': ['available']
          }
          ]
          )
          for vol in volumes['Volumes']:
              #print (vol)
              now = datetime.datetime.now(timezone.utc)
              difference = now - vol['CreateTime']
              #print(difference.days)
              if difference.days >= int(threshold_days):
                 print(f"VolumeId: {vol['VolumeId']} , VolumeSize: {vol['Size']} , CreationTime: {vol['CreateTime']} , Age: {difference.days}")
except ClientError as e:
    print(e)