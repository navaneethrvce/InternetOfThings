import subprocess
def add_rule(s_ip,d_ip):
	subprocess.call(['iptables','-A','FORWARD' ,'-s', s_ip , '-d',d_ip ,'-j','REJECT'])
add_rule('10.42.0.161', '31.13.73.36')
