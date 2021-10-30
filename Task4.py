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

caller_set = set()
non_telemarketer_set = set()

for call_records in calls:
    caller, callee = call_records[0], call_records[1]
    caller_set.add(caller)
    non_telemarketer_set.add(callee)

for text_records in texts:
    sender, sendee = text_records[0], text_records[1]
    non_telemarketer_set.add(sender)
    non_telemarketer_set.add(sendee)

telemarketer_set = sorted(caller_set - non_telemarketer_set)
print("These numbers could be telemarketers: ")
print("\n".join(telemarketer_set))

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

