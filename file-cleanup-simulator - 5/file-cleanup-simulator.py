import os
from datetime import datetime
import time

## Fetch Inputs

dir_path = input("Please enter the directory path: ")

thresholddays = int(input("Please enter the Threshold days that file should be compared against: "))

## Validate input

if not all([dir_path, thresholddays]):
    print ("Empty Inputs detected for Directory path or Threshold days, Please provide inputs to proceed further")
    exit

if not os.path.isdir(dir_path):
    print("Input Directory provided doesn't exists, Provide Valid input directory")
    exit

## Implementation Logic

for root, dirs, files in os.walk(dir_path):
    for file in files:
        full_file_path = os.path.join(root, file)
        #print (full_file_path)

        # Calculate last modification time of a file
        modification_timestamp = os.path.getmtime(full_file_path)

        # Convert the timestamp to a datetime object
        modification_date = datetime.fromtimestamp(modification_timestamp)

        # Get the current date and time
        current_date = datetime.now()

        # Calculate the difference, resulting in a timedelta object
        difference = current_date - modification_date
        if difference.days > thresholddays:
           print (f"File Name:  {full_file_path} , Number of days old: {difference.days}")