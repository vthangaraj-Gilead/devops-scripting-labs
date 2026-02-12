# Problem <6>: AWS EC2 Inventory Report

## Scenario

- Need Ec2 instance summary without loggin into AWS console

---

## Objective

- Summarize Instance details for a given AWS region

---

## Inputs

- AWS Region

---

## Expected Output

For all the instances within a given aws regiona, output should be

- Instance ID
- Instance Type
- Instance State
- Instance Public IP
- Instance Availability Zone

---

## Constraints & Assumptions

- AWS Linux Ec2 Server
- AWS Cli installed
- Server has iam role permissions to describe instance details

---

## Suggested Approach

- Validate Input & Exit if invalid or Empty Input is passed
- Use Ec2 Describe instances aws cli command to fetch the instance deails f

---

## Bash vs Python Consideration

- Expected Output can be achieved by aws cli command, so bash script is preferred

---

## Edge Cases to Consider

- This script doesn't provide resource count symmary, only print ec2 instance details
- Script doesnt handle logic if ec2 instances are empty for a given region
- Output in text  for ec2 describe command sorts results in alphabetical order by column, no matter the query order, implementaion logic looping variables are assigned in that matter. Script should be updated if this outcome is not preferred.

---

## Learning Outcome

- AWS Cli command & Working of `--query` argument
- Validating if a given region is a AWS available region