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


time_spent_on_phone = {}
for calls_record in calls:
    time_spent_on_phone[calls_record[0]] = time_spent_on_phone.get(calls_record[0], 0) + int(calls_record[3])
    time_spent_on_phone[calls_record[1]] = time_spent_on_phone.get(calls_record[1], 0) + int(calls_record[3])

telephone_number = max(time_spent_on_phone, key=time_spent_on_phone.get)
max_total_time = time_spent_on_phone[telephone_number]
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