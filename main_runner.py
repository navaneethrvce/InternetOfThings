import os
from add_firewall_rule import add_rule
import time
import itertools
ip_address = {}
while(1):
	ip_list = []
	os.system('python ping_host.py > hosts.txt')
	fp = open('hosts.txt','r')
	for line in fp.readlines():
		if line not in ip_list:
			ip_list.append(line.strip())

	#for ip in ip_list:
	#	for dest_ip in ip_list:
	#			if dest_ip != ip:
	#				if ip.strip() not in ip_address or (ip.strip() in ip_address and ip_address[ip.strip()] != dest_ip.strip()):
	#					add_rule(ip.strip(),dest_ip.strip())
	#					ip_address[ip.strip()] = dest_ip.strip()
	#				if dest_ip.strip() not in ip_address or (dest_ip.strip() in ip_address and ip_address[dest_ip.strip()] != ip.strip()):
	#					add_rule(dest_ip.strip(),ip.strip())
	#					ip_address[dest_ip.strip()] = ip.strip()

	for ele in ip_list:
		print ip_address
		if ele in ip_address:
			#ip_address[ele] = 0
			continue
		ip_address[ele] = 0
		if len(ip_address) > 1:
			for key,value in ip_address.items():
				if ip_address[key] != 0:
					add_rule(key,ele)
					add_rule(ele,key)
			ip_address[ele] = 1
		else:
			ip_address[ele] =1		
	#print set(itertools.combinations(ip_list,2))
	fp.close()
	time.sleep(20)
