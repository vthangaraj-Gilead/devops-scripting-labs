# Problem <1>: System Health Snapshot

## Scenario

> During routine operations, devops engineers are expected to check system status before actual implementation

---

## Objective

Print basic status checks that are needed to check as a single summary output instead of executing by commands.

---

## Inputs

No Inputs required for this scenario

---

## Expected Output

- Hostname of the server
- Current Date & Time
- Current Disk Usage
- Current Meory Usage
- Uptime of the server

---

## Constraints & Assumptions

- Linux environment
- AWS Ec2 instance
- Execution permissions for the script provided(755)

---

## Suggested Approach

- Use `echo` to print output of the commands via script execution
- consider printing in human readable format for more readability (for memory & disk usage print using `-h`)

---

## Bash vs Python Consideration

- This scenario involves linux fundamentals. So Bash is preferred

---

## Edge Cases to Consider

- System Health checks varies as per environment needs - This script covers basic health checks only.

- Script may fail executing, if necessary permissions not provided (755 - execution permission)

---

## Learning Outcome

- Bash fundamentals
- Linux health check commands & ouput printing
