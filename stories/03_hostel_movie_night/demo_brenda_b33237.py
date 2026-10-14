"""
Extension 1 demo: Short comedy clip.
Author: IYAMUMPAYE BRENDA B33237

Run from the main repository folder:
  Windows:  py -3 stories/03_hostel_movie_night/demo_paula_XXXXXXX.py
"""
from story import ComedyClip, MovieNight

clip = ComedyClip("Kampala Giggles")
print(clip.describe())
print("Expected: Kampala Giggles: 50 MB at Mukono hostel lounge")

# Normal case: enough data
faith = MovieNight("Faith", 500)
print(faith.enjoy(clip))
print("Expected: Faith's group enjoys Kampala Giggles. Data left 450, activities 1")
print("Actual: data left", faith.bundle.remaining, "activities", faith.activities)

# Refused case: not enough data
david = MovieNight("David", 40)
print(david.enjoy(clip))
print("Expected: refused. Data left 40, activities 0")
print("Actual: data left", david.bundle.remaining, "activities", david.activities)

# Boundary case: exactly 50 MB
grace = MovieNight("Grace", 50)
print(grace.enjoy(clip))
print("Expected: allowed. Data left 0, activities 1")
print("Actual: data left", grace.bundle.remaining, "activities", grace.activities)
