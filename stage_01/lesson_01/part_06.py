import re

first_day_kilometers = input('Please enter you distance in kilometer at first day: ')
expected_kilometers = input('Please enter you expected kilometers per one day: ')

pattern = r'^\d+$'

if not re.match(pattern, first_day_kilometers) or not re.match(pattern, expected_kilometers):
    raise TypeError('You are enter invalid kilometers. Please verify arguments and try again.')

first_day_kilometers = int(first_day_kilometers)
expected_kilometers = int(expected_kilometers)

if expected_kilometers <= first_day_kilometers:
    print(f'The distance {expected_kilometers} you walk in first day ;)')
    exit(0)

actual_kilometers = float(first_day_kilometers)
active_days = 1

while True:
    actual_kilometers = actual_kilometers * 1.1
    active_days = active_days + 1

    # Only for debug
    print(f'On %d day you are run %.2f km.' % (active_days, actual_kilometers))

    if actual_kilometers >= expected_kilometers:
        print(f'The distance {expected_kilometers} km. you will run on {active_days} on day.')
        break

    if active_days > 1000:
        raise TypeError('Too long calculation.')

