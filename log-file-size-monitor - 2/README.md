# Problem <2>: Log File Size Monitoring

## Scenario

 - Applications hosted via Ec2 have logging enable to store in ec2 local stoage(EBS)(if not configured to store in external storage - S3, cloud watch)
 - Over time  application logs, system logs files size increases resulting in disk pressure in the ec2 server.

---

## Objective

- Identify large files for a target directory, so the Team can validate and take necessary action(Delete / Log Rotate, etc...)

---

## Inputs

- Target Directory Input
- Threshold Size in MB(MegaBytes) Input

---

## Expected Output

- Files in Target Directory that have size > Threshold size

---

## Constraints & Assumptions

- AWS EC2 Linux environment
- Threshold Size Input in MegaBytes (for human understanding instead of using bytes)
- Execution Permissions provided for the script (755)
---

## Suggested Approach

Use `find` command to search through files and use flags of `find` command to compare the size and return the large files

**Key Command**: `find . -type f -size +10M` ## Return files in current directory > 10MB

---

## Bash vs Python Consideration

- Expected outcome can be achieved using linux command, hence bash is preferred

---

## Edge Cases to Consider

- Output of this script only list files - not their sizes
- No destructive activity is performed, only list the large files - still need human intervention for cleanup
- Inputs for Threshold size are only provided in MB, script needs to be updated for other size requirements

---

## Learning Outcome

- Fetch Inputs at run time using `read`
- Validate Empty Inputs
- List files in a directory using `find`