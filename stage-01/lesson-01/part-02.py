import re

time_in_seconds = input('Please enter time in seconds (only int numbers allowed): ')

if not re.match(r'^\d+$', time_in_seconds):
    raise TypeError('You\'r are enter invalid seconds. Please enter only int digits')

time_in_seconds = int(time_in_seconds)

hours = int(time_in_seconds / (60 * 60))
leave_seconds = time_in_seconds - (hours * 3600)

minutes = 0

if leave_seconds > 0:
    minutes = int(leave_seconds / 60)
    leave_seconds = leave_seconds - (minutes * 60)

print(f'In H:m:i you are enter {hours} hours {minutes} minutes and {leave_seconds} seconds')
