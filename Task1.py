"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

list_of_phone_numbers = []

for row in texts:
    if row[0] not in list_of_phone_numbers:
        list_of_phone_numbers.append(row[0])
    if row[1] not in list_of_phone_numbers:
        list_of_phone_numbers.append(row[1])

for row in calls:
    if row[0] not in list_of_phone_numbers:
        list_of_phone_numbers.append(row[0])
    if row[1] not in list_of_phone_numbers:
        list_of_phone_numbers.append(row[1])

print("There are %s different telephone numbers in the records." % len(list_of_phone_numbers))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
