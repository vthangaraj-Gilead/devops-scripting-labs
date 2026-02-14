#!/bin/bash

set -o pipefail

read -p $'Enter the threshold size:\n' threshold

if [ -z "$threshold" ]; then
   echo "Empty Threshold size. Provide threshold to validate"
   exit
fi

df -h | awk 'NR>1 {print $6, $5}' | while read mount usage; do
    USAGE=$(echo $usage | sed 's/%//')
    # Compare the usage with the threshold
    if [ "$USAGE" -ge "$threshold" ]; then
        echo "Alert: Mount point $mount has reached ${USAGE}% usage  (threshold: $threshold%)"
    fi
done