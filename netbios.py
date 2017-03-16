import subprocess
def netbios_resolver(ip_addr):
	output = subprocess.check_output(['nbtscan',ip_addr])
	s = output.split()
	if len(s) > 17:
		if len(output.split('\n')) > 2:
			ret_val = s[17] + " " + s[18]
			print 'RET_VAL in netbios :' + ret_val
			return ret_val
		else:
			return ""
	else:
		print "NBT Scan falied\n"
		return ""
#print netbios_resolver('10.42.0.221')
	
