import subprocess
import json
region_validate_command = ['aws', 'ec2',  'describe-regions', '--query',  'Regions[].RegionName',  '--output', 'json']
filter_sg_command = ['aws', 'ec2', 'describe-security-groups', '--filters', "Name=ip-permission.from-port,Values=22", "Name=ip-permission.to-port,Values=22", "Name=ip-permission.cidr,Values='0.0.0.0/0'", '--query', 'SecurityGroups[*].{SecurityGroupID:GroupId,IpPermissions:IpPermissions[*].{FromPort:FromPort,ToPort:ToPort,CIDR:IpRanges[*].CidrIp}}']


## fetch input

region = input("Enter the AWS Region to validate the SG: ")

## Validate Input
if not region:
   print ("Empty AWS Region Input provided. Please Try again!")
   exit
else:
   try:
       region_list=subprocess.run(region_validate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) #since using python<3.7 universal_newlines is used
       region_json=json.loads(region_list.stdout)
       #print(region_json)
       if region not in region_json:
          print("Invalid AWS Region Input.Please Try Again")
          exit
       else:
          print("Valid AWS Region Input")
          ## Implementation Logic
          risk_sg_list=subprocess.run(filter_sg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
          risk_sg_json=json.loads(risk_sg_list.stdout)
          #print(risk_sg_json)
          # Print Each JSON Object Separately in new line
          for sg in risk_sg_json:
              print(json.dumps(sg))
   except Exception as e:
      print(e)