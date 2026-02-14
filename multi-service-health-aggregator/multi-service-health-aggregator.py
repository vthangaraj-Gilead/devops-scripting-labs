import psutil
import subprocess

## Check Memory Usage

def get_memory_usage() -> int:
    memory = psutil.virtual_memory()
    #print(int(memory.percent))
    print("===== Memory Usage =====")
    print()
    if int(memory.percent) >= 75:
       print ("ALERT: High Memory Usage Detected ...")
       return 1
    else:
       print (f"Memory Usage is Optimal at {memory.percent}%")
       print()
       return 0

## Check Disk Usage

def get_disk_usage() -> int:
    print("===== Disk Usage =====")
    print()
    command = ['df', '-h']
    disk_usage = subprocess.run(command, capture_output=True, text=True)
    lines = disk_usage.stdout.strip().split('\n')
    flag = 0
    for line in lines[1:]:
        part = line.split()
        usage = part[4]
        mounted_on  = part[5]
        if int(usage.replace("%", "")) >= 80:
           print(f"ALERT --> {mounted_on} Usage is at {usage}")
           flag = 1
    #print(flag)
    if flag == 0:
       print("Disk Usage is Optimal")
       print()
       return 0
    else:
       print()
       return 1


## Check Service Status

def check_service_status() -> int:

    monitor_services=['docker', 'sssd', 'sshd', 'abcd']
    print("===== Critical Service Status =====")
    print()
    flag = 0
    for i in monitor_services:
        #print(type(i))
        response = subprocess.run(['systemctl', 'is-active', i], capture_output=True, text=True)
        if not response.stdout.strip() == 'active':
           print(f"ALERT --> {i} Service is not Active")
           flag=1
    if flag == 0:
       print("All Critical Services are in Active State")
       print()
       return 0
    else:
       print()
       return 1

if __name__ == "__main__":
   x = get_memory_usage()
   y = get_disk_usage()
   z = check_service_status()
   print("====== Generating consolidated Summary =====")
   print()
   if any([x,y,z]):
      print("Action: Immediate Action Required!")
   else:
      print("System Health is in optimal state")