#/bin/bash

echo -e "============== SYSTEM HEALTH CHECK ==============\\n"


echo "HOSTNAME:"
echo -e "$(hostname)\\n"


echo "DATE & TIME:"
echo -e "$(date)\\n"

echo "DISK USAGE:"
echo -e "$(df -h)\\n"

echo "MEMORY USAGE:"
echo -e "$(free -h)\\n"

echo "UPTIME:"
echo "$(uptime)"