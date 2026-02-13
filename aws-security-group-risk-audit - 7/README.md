# Problem <7>: AWS Security Group Risk Audit

## Scenario

- There are cases where team temporarily open security group inbound rule ports like 22(SSH) to Anywhere for testing and forget to revert back the changes.
- This makes the server vulernable and prone to external attacks.

---

## Objective

- Identify Security Groups which has inbound rules with Port 22(SSH) and the Source CIDR is opened to '0.0.0.0/0'.

---

## Inputs

- AWS Region

---

## Expected Output

Seucirty groups which has 22 port open to '0.0.0.0/0'. will print the following:

- Security Group ID
- From Port
- To Port
- CIDR

**Note**: Even though the implementation logic filters only the sg with port 22 and open to icdr '0.0.0.0/0' we will still print the same port and cidr information in output, in future we can improve the script logic to multple ports and Source CIDR's

---

## Constraints & Assumptions

- AWS EC2 Linux
- AWS Cli installed
- Python Installed
- IAM Permisisons to Describe Security Groups
- Execution Permissions for the script (755)

---

## Suggested Approach

- Fetch AWS Region Input from User
- Validate the Input
- Using `Subprocess.run()` in Python, run the aws cli commad which filters the Security groups that has port 22 and cidr open to '0.0.0.0/0'
- Capture the Subprocess output in a variable and convert into python object using `json.loads()`
- Print Pretty Output JSON line by line by using `for` loop and `json.dumps()`

---

## Bash vs Python Consideration

- Implementation for this script can be easily done in bash
- To improve learning curve & Json Manipulation in python is easy, script is implemented in python.

---

## Edge Cases to Consider

- If there are no SG's with inbound rule port 22 for cidr '0.0.0.0', script returns empty
- Script logic only checks for port 22 opened for cidr '0.0.0.0/0'. For Custom Ports or CIDR. Script logic needs to be updated.

---

## Learning Outcome

- Json Parsing in Python
    - Json.loads() - convert Output Json string into python object (`{}`)
    - Json.dumps() - convert python object to Json string
- Subprocess.run() in Python to run cli commands