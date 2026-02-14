# Problem: Orphan AWS EBS Volume Detector

## Scenario

- A Cloud Team might manage ec2 servers in multiple aws accounts and  in multiple regions in an aws account, it is really hard to track unused ebs volumes which silently incurs cost unless we login to console for each account and check the EBS volumes status.

---

## Objective

- Identify the EBS volumes in `Available` status which has aged more than the given input threshold days.

---

## Inputs

- AWS Region
- Threshold Days

---

## Expected Output

Volumes aged more than or equal to the threshold days will be printed with following output

- Volume ID
- Size
- Creation Time
- Age

---

## Constraints & Assumptions

- AWS Ec2 Linux Environment
- Python > 3.9 is installed (for stable boto3 implementation)
- Pip & Boto3 is installed
- Ec2 has IAM permissions to describe volumes

---

## Suggested Approach

- Fetch the AWS Region & Threshold days as input
- Create a Boto3 client for Ec2 & pass the input region
- Using Describe Region from boto3 client, Validate the AWS Region input
- Using Describe volume, use filter to fetch only volumes in Available state
- Using Datetime in Python, calculate the time delta and compare it with Threshold days input
- Print VolumeId, VolumeSize, CreationTime, Age only if the time delta >= Threshold days input



---

## Bash vs Python Consideration

- Script is implemented using Python to handle json outputs easily

---

## Edge Cases to Consider

- Empty Output if there is no volumes >= Threshold days
- Error if Threshold days input is non integer

---

## Learning Outcome

- Boto3 Implementation
- Creation Time with Timezone
    Note: since the creation time is timezone aware, while calculating the time
          delta the now time should be in timezone format, then we can calucalte the delta more accurately.