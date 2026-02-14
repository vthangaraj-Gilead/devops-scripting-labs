# Problem: AWS Instance State Drift Detector

## Scenario

- Sometimes a ec2 instance is expected to be always in `running` state due to scheduled background jobs, cron jobs etc.
- Due to accidental activity or due to other automation scripts, the instances can be stopped.

---

## Objective

- Identify the instances with  a specific filter is in `running` or `stopped` state.

---

## Inputs

- No Inputs required

---

## Expected Output

- InstanceId's of Instances in `stopped` state will be printed as output

---

## Constraints & Assumptions

- AWS Ec2 Linux Environment
- Python > 3.9 & pip, boto3 installed.
- Ec2 instance has IAM permissions to describe ec2 instances for us-west-2 region


---

## Suggested Approach

- Create a boto3 client for ec2 and configure us-west-2 region
- using describe instances, filter ec2 instances based on state='stopped' &&  particular tag value
- Print instance id of those instances.

---

## Bash vs Python Consideration

- Output data can be easily handled in Python, hence python is preffered

---

## Edge Cases to Consider

- Script can only list InstanceId's of instances in stopped state, script needs to be improved if those instances needs to started & run background jobs
- If required tag value is not added to the ec2 instance, then script will not be able to identify its state.

---

## Learning Outcome

- Boto3 Implementation
- Nested For loops