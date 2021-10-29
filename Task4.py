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

import pandas as pd

texts_df = pd.DataFrame(texts, columns=['sender', 'receiver', 'timestamp'])
calls_df = pd.DataFrame(calls, columns=['caller', 'receiver', 'timestamp', 'duration'])

telemarketer_list = list()
for caller in calls_df['caller']:
    if (caller not in calls_df['receiver']) and (caller not in texts_df['sender']) \
            and (caller not in texts_df['receiver']):
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

