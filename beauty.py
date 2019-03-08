#beautifulsouptest.py

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com")
print(r.status_code)
print(r.headers)

content = r.content
soup = BeautifulSoup(content,"html.parser")
#soup = BeautifulSoup(content,"lxml")
links = soup.find_all("a")
print(links)
print("\n")

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs["href"])

