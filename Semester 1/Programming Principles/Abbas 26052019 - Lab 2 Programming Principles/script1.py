totalSec = int(input("Enter the amount of seconds: "))

time_hour = totalSec//3600
time_minutes = totalSec % 36001 //60
time_seconds = totalSec%60

print(f"The time in seconds converted to hour, minute, seconds is {time_hour:02d}:{time_minutes:02d}:{time_seconds:02d}")