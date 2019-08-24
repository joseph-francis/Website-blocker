from datetime import datetime
import time

host_path = "/private/etc/hosts"
redirect = "73.232.161.226"
website_lists = ["www.facebook.com", "facebook.com"]

now = datetime.now()

while True:
    if datetime(now.year, now.month, now.day, 8) < now < datetime(now.year, now.month, now.day, 16):
        print("Working hours")
    else:
        print("Chill hours")
    time.sleep(5)



