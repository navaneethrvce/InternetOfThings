import requests
import json
from bs4 import BeautifulSoup


file  = open("findBlackList.txt","a+")

r = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data = {'ip':'204.140.180.2'})

#print r.text
soup = BeautifulSoup(r.text,"html.parser")
table = soup.find("table", attrs= {"class" : "table table-striped table-bordered"})
headings = [th.get_text() for th in table.find("tr").find_all("td")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    file.write(str(dataset))
    datasets.append(dataset)

print datasets