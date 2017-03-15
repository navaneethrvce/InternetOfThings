import subprocess
def add_rule(s_ip,d_ip):
	print "In function -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- "+s_ip+"       "+d_ip
	subprocess.call(['iptables','-A','FORWARD' ,'-s', s_ip , '-d',d_ip ,'-j','REJECT'])

