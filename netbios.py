import subprocess
def netbios_resolver(ip_addr):
	output = subprocess.check_output(['nbtscan',ip_addr])
	#print output
	if len(output.split('\n')) > 3:
		return output.split('\n')[4].split()[1]
	else:
		return ""
print netbios_resolver('10.42.0.221')
	
