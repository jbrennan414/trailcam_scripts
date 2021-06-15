from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

with open("/home/pi/trailcam_scripts/log.txt", "a") as f:
  f.write(f"Still alive {month}/{day}/{year} {hour}:{minute} \n")
