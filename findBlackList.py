import requests
import json
from bs4 import BeautifulSoup
from add_firewall_rule import add_rule

fileInput =  open("result.txt", "r")

blackListedIP = {}
allowedIP = {}



file  = open("findBlackList.txt","a+")
def isBlackList( s_Ip, d_IP):

	print("INSIDE ")

	r = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data = {'ip': d_IP})



	#print r.text
	soup = BeautifulSoup(r.text,"html.parser")
	table = soup.find("table", attrs= {"class" : "table table-striped table-bordered"})
	
	if table != None:

		headings = [th.get_text() for th in table.find("tr").find_all("td")]

		datasets = []
		for row in table.find_all("tr")[1:]:
		    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
		    file.write(str(dataset))
		    datasets.append(dataset)

		getIPSplit = str(datasets[0][1]).split(",")
		print "This is the IP " + getIPSplit[1]

		if "BLACKLISTED" in getIPSplit[1]:
			return True
		else:
			return False




	else:
		print "Invalid IP"
		return False




for line in fileInput:
	dataSplit = line.split(",")
	print dataSplit
	sourceIP = dataSplit[0]
	destinationIP = dataSplit[2]
	print  sourceIP + " " + destinationIP
	if sourceIP in allowedIP:
		if allowedIP.get(sourceIP) == destinationIP:
			print ("Allowed")
	elif sourceIP in blackListedIP:
		if(blackListedIP.get(sourceIP == destinationIP)):
			print "Refused"
	else:
		if isBlackList(sourceIP, destinationIP):
			blackListedIP[sourceIP] = destinationIP
			print "You are Blacklisted"
			add_rule(sourceIP,destinationIP)
		else:
			allowedIP[sourceIP]= destinationIP
			print "You are Allowed"
		# fileInput.write(sourceIP] + "  " + dataSplit[1])


print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

count = 0;

for iter in blackListedIP:
	count += 1
	print iter + " " + str(count)

print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
count = 0;
for iter in allowedIP:
	count+=1
	print iter + " " + str(count)
