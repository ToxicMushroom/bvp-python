seconds = int(input("Time in seconds: "))

DAY_SECONDS = 86_400
HOUR_SECONDS = 3_600
MINUTE_SECONDS = 60

days = seconds // DAY_SECONDS
seconds -= days * DAY_SECONDS

hours = seconds // HOUR_SECONDS
seconds -= hours * HOUR_SECONDS

minutes = seconds // MINUTE_SECONDS
seconds -= minutes * MINUTE_SECONDS

print("{} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
