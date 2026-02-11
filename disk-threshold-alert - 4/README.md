# Problem <4>: Disk Threshold Alert

## Scenario

- Disk Space silently increase over time if not actively monitored
- Leaving them unattended leads to node health risk.

---

## Objective

- Identify the mounts that have >= a specfic usage

---

## Inputs

- Threshold Size input (Number) from user.

## Expected Output

- Mounts with usage % that has >= Threshold size

---

## Constraints & Assumptions

- AWS EC2 Linux environment
- Threshold Size input is Number (80 not 80%)
- Execution Permissions for the script (755)

---

## Suggested Approach

- Validate User Inputs
- Use `df -h` to check the current mounts and usage
- Parse the output using linux parsing commands (`awk` and `sed`) and compare it with Threshold size
- If Filesystem size >= Thresold size, print Alert message, if not skip

**Key Command**: `df -h` ## Print the current mountd file system, size, usage, etc in human readable format.

---

## Bash vs Python Consideration

- Expected outcome can be achieved using linux commands. Hence Bash is preferred.

---

## Edge Cases to Consider

- Only compares the Mount usage with Threshold usage and list mounts, further action needs human intervention
- Doesn't segregate filesystems - print all files systems (including tmp, external file systems like efs) which has>= Threshold size.

---

## Learning Outcome

- Loop statements
    - For loops - use when the items are finite
    - While loops - loops through commands until a given statement is true, if condition fails loop exit
    - until loops - opposite of while loop, executes until a given statement is false, if condition becomes true, loop exit
- Text parsing
    - awk - used for data extraction
    - sed - used for find and replace in text operations