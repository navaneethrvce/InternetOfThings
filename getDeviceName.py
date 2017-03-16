from cluster import categorize
from netbios import netbios_resolver



deviceCategory = open("deviceCategory.txt","a+")

#getIPFromFile = open ("hosts.txt")

def getDevName(line):

#	for line in getIPFromFile:
	res = netbios_resolver(line)
	if res != "":
		name = res.split()[1]
		cat = categorize(name,0)
		deviceCategory.write(res + ' ' + cat +'\n')		#writes category
		deviceCategory.flush()
		return (res + ' ' + cat + '\n')
