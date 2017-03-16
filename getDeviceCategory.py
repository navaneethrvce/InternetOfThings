import sys
from add_firewall_rule import add_rule

deviceCat = open("deviceCategory.txt","a+")
blackListIP = ['www.allpornsites.com','www.usa.gov','www.cia.gov','www.fbi.net','www.sunnyleone.com']

for line in deviceCat:
	cat = line.split()[2]
	switch(cat):
		case 'health' : callHealth(line.split()[0])
		case 'enter'  : callEnter(line.split()[0])
		case 'home'   : callHome(line.split()[0])
		case 'generel': callgenerel(line.split()[0])

def callHealth(s_ip):
	add_rule(s_ip,'66.220.144.0')

def callEnter(s_ip):
        add_rule(s_ip,'104.25.249.109')

def callHome(s_ip):
        add_rule(s_ip,'23.208.150.150')

def callHgenerel(s_ip):
        add_rule(s_ip,'68.210.154.1')
