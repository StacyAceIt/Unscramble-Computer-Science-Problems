"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

max_total_time = 0
max_record_index = None
for record_index, record in enumerate(calls):
    if int(record[3]) > int(max_total_time):
        max_total_time = record[3]
        max_record_index = record_index

telephone_number = calls[max_record_index][0]

print("%s spent the longest time, %s seconds, on the phone during September 2016."
      % (telephone_number, max_total_time))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""