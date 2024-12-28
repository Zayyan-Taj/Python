# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
distance_miles = 10
time_minutes = 30
time_seconds = 30

time_hours = time_minutes / 60 + time_seconds / 3600
distance_km = distance_miles * 1.6

average_speed = distance_km / time_hours

print("The average speed is", average_speed, "km/h")

