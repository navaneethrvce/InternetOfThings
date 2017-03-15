import os

fw = open('result.txt',"w")

while(1):
	result = os.popen("sudo tcpdump -n -i  wlp0s20u12 not arp and not rarp -c 1 | awk '{print $1,$2,$3,$5}' ").read()
	token = result.split()
	time,proto,source,dest = token[0],token[1],token[2],token[3]
	print source
	index = source.rfind('.')
	srcPort = source[index+1:]
	print srcPort
	source = source[:index]
	index = dest.rfind('.')
	dstPort = dest[index+1:]
	dest = dest[:index]
	dstPort = dstPort[:-1]
	print 'source :',source,'srcPort',srcPort,'Dest',dest,'DestPort',dstPort
	fw.write(source+','+srcPort+','+dest+','+dstPort+','+time+','+proto+'\n')

fw.close()
