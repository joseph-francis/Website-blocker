from datetime import datetime
import time

host_path = "/private/etc/hosts"
redirect = "73.232.161.226"
web_lists = ["www.facebook.com", "facebook.com", "www.google.com", "google.com"]

now = datetime.now()

while True:
    if datetime(now.year, now.month, now.day, 8) < now < datetime(now.year, now.month, now.day, 17):
        print("Working hours")
        with open(host_path, "r+") as file:
            content = file.read()

            for website in web_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_lists):
                    file.write(line)
            file.truncate()

    time.sleep(5)



