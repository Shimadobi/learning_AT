import requests
import threading


def dl_site(site):
    while True:
        req = requests.get(site)
        with open('task04-03-site.txt', 'w', encoding="utf-8") as file:
            file.write(req.text)


t = threading.Thread(target=dl_site, args=('https://epam.com',))
t.daemon = True
t.start()
