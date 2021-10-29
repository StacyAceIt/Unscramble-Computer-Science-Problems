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

text_sender = []
text_receiver = []
call_receiver = []
for index, text_record in enumerate(texts):
    text_sender.append(text_record[0])
    text_receiver.append(text_record[1])
    if index < len(calls):
        call_receiver.append(calls[index][1])

telemarketer_list = list()
for call_record in calls:
    caller = call_record[0]
    if (caller not in text_sender) and (caller not in text_receiver) and (caller not in call_receiver):
        telemarketer_list.append(caller)

telemarketer_sorted_set = sorted(set(telemarketer_list))

print("These numbers could be telemarketers: ")
print("\n".join(telemarketer_sorted_set))

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

