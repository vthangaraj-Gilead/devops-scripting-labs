#!/bin/bash

set -o pipefail

## Fetch User  Inputs

read -p $'Enter Target Directory Path:\n' DIRECTORY
read -p $'\nEnter Threshold size to be validated in MB:\n' THRESHOLD

## Validate Inputs
if [[ -z "$DIRECTORY" || -z "$THRESHOLD" ]]; then
   echo "No Target directory or Threshold size input provided..Please provide inputs to validate files..."
   exit
fi

## Implementation Logic

echo -e "\\n=============== Large Files > than $THRESHOLD MB ===============\\n"

find "$DIRECTORY" -type f -size +${THRESHOLD}M