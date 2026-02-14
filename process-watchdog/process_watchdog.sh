#!/bin/bash

set -o pipefail

## Fetch User Input

read -p $'\nEnter the process to be monitored:\n' pid

## Validate Inputs

if [ -z "$pid" ]; then
   echo "Detected Empty Input. Provide Inputs to monitor the requires process!"
   exit
else
   if ! pgrep -f "$pid" > /dev/null; then
      echo -e "\\nWARNING process $pid is not running\\n"
      echo -e "Exit code of pgrep - $?\\n"
   else
      echo -e "\\nProcess $pid is RUNNING"
   fi
fi