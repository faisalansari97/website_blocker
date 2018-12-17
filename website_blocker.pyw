import time
from datetime import datetime as dt

host_temp = "D:\Programs\Python Projects\Python Projects\website_blocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
websites = ["www.facebook.com", "www.instagram.com", "www.twitter.com"]
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

