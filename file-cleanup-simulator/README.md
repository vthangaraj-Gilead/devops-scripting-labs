# Problem: File Cleanup Simulator

## Scenario

- Unnecessary files or least accessed files are piled up over time
- Leaving them be causes increase in disk usage

---

## Objective

- Identify & List files by age > No of days given as input (List Only)

---

## Inputs

- Directory Path
- No of Threshold days

---

## Expected Output

 - List all the files with age > than threshold days

---

## Constraints & Assumptions

- AWS EC2 Linux environment
- Python should be installed in the server
- Execution permissions for the script (755)

---

## Suggested Approach

- Fetch the input directory and Threshold days as input
- Validate input is empty and the given directory is valid path in the server
- Calculate the last modification date of all files in the directory
- Caculate the no of days the file has aged from last modification date till now
- Compare the file age days with threshold daysif greater print the file with path & no of days it is old

---

## Bash vs Python Consideration

- Time Calculations can be easily done using python hence python is preferred.

---

## Edge Cases to Consider

- Threshold days Input can only accept integer values
- This script only list files based on threshold days doesnt perform any destructive behaviour
- This script logic is based on the last modification date of the file not the creation time of the file
- If none of the files are greater than the threshold days, the script returns empty output

---

## Learning Outcome

- Writing scripts in Python
- Fetching inputs at run time in python
- List files in a directory using `os` module
- calculate time for file using `time` module
- If and Loop Conditions