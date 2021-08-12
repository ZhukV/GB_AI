import re

ratings = [7, 5, 3, 3, 2]

new_rating = input('Please enter a new rating (between 0 and 9): ')

if not re.match(r'^\d$', new_rating):
    raise TypeError('Only one digit 0-9 supported.')

new_ratings = ratings.copy()
new_ratings.append(int(new_rating))

sorted_ratings = sorted(new_ratings, reverse=True)

print(f'Old ratings: {ratings}')
print(f'New ratings: {sorted_ratings}')
