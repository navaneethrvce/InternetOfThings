# from urllib import urlopen
# story = urlopen('https://www.python.org')
# story_words = []
# file  = open("output.txt","w")

# for line in story:
# 	file.write(story_words)


# for line in story:
#     line_words = line.split()
#     for words in line_words:
#         story_words.append(words)

#     file.write(story_words)

import requests,json
from bs4 import BeautifulSoup

r = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data = {'ip':'204.140.180.2'})

soup = BeautifulSoup(r,"html.parser")
table = soup.find("table", attrs= {"class" : "label label-success"})
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

print datasets
