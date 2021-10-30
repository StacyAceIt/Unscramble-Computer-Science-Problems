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

phone_numbers_set = set()

for row in texts:
    phone_numbers_set.add(row[0])
    phone_numbers_set.add(row[1])

for row in calls:
    phone_numbers_set.add(row[0])
    phone_numbers_set.add(row[1])

print("There are %s different telephone numbers in the records." % len(phone_numbers_set))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
