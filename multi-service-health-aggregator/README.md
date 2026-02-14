# Problem: Multi Service Health Aggregator

## Scenario

- Before performing patching or any operational activities, Team often need to do a health check before or after implementation to ensure System is in optimal state

---

## Objective

- Identify Disk, Memory & Critical Services and check whether they are in optimal state and return a summary of current status

---

## Inputs

- No Inputs Required

---

## Expected Output

- Print Memory Usage Status
- Print Disk Usage Status
- Print Critical service Status

---

## Constraints & Assumptions

- AWS EC2 Linux Environment
- Python > 3.9 installed and required python modules (psutils) installed

---

## Suggested Approach

- For Memory Usage
    - Use psutils() python module and check the memory usage in % and compare with Threshold %
- For Disk Usage
    - Use Subprocess command to execute `df -h` command and use split() to separate the output line by line and loop through get fetch the Use% and compare with threshold %
- For Critical Service Status
    - Use SubProcess to check whether a predefined list of critical services are running or not
- Set Exit code for each function and Print a consolidated summary output

---

## Bash vs Python Consideration

- Script is implemented using python to improve python scripting learning curve

---

## Edge Cases to Consider

- Script returns only consolidated health checks in a ec2 instance. For further action human intervention is required.
- For Critical services, only predefined services are checked, script needs to be updated for including other services to be monitored

---

## Learning Outcome

- Psutils usage
- Usage of split(), replace(), strip()
- repr(output) - shows hidden characters in a string