# Problem : Linux Process Watchdog

## Scenario

Some Linux processes are always expected to run like system background process, monitoring process, scheduled job process. But Processes may stop running if they face intermittent issues

---

## Objective

- Identify a specific process is running or not running.

---

## Inputs

- Process name as input from user

---

## Expected Output

- Print Message if process is running
- Print Message if process is not running

---

## Constraints & Assumptions

- AWS EC2 Linux environment
- User is aware of the process name to be provided as input
- Execution Permissions for this script (755)


---

## Suggested Approach

- Validate input is empty or value provided
- Identify given input process is running or not using pgrep [we can also use ps-ef or ps -a  but while grepping, the grep output is also displayed]
- If process is running, print message
- If process is not running, print message

**Key Command**: `pgrep -f "sh"` ## Checks if sh process is running or not

---

## Bash vs Python Consideration

- Expected outcome can be achieved using linux command. So Bash is preffered

---

## Edge Cases to Consider

- User is expected to be aware of the process name
- No restart behaviour - this script only checks the status of process. Human intervention is required if a non running process needs to be restarted
- If a process is not running, this script doesnt capture `why`, only prints the current status of the given process

---

## Learning Outcome

- Check process status using `pgrep`
- Use nested conditional statements