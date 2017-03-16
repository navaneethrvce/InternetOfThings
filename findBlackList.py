import requests
import json
from bs4 import BeautifulSoup
from add_firewall_rule import add_rule
import time
from collections import defaultdict
from getDeviceName import getDevName


blackListedIP = defaultdict()
allowedIP = defaultdict()



fileBlackListedIP = []
fileAllowedIP = []



file  = open("findBlackList.txt","a+")
fileOutput = open("BlackList.txt","a+")



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


def getNextData(lineNum):

        fileInput =  open("result.txt", "r")
        #fileOutput = open("BlackList.txt","a+")
        count =0
        for line in fileInput:
                if count<lineNum:
                        count += 1
                        continue
                dataSplit = line.split(",")
                print dataSplit
                sourceIP = dataSplit[0]
                destinationIP = dataSplit[2]
                print  sourceIP + " " + destinationIP
                if sourceIP in allowedIP:
                        if allowedIP.get(sourceIP) == destinationIP:
                                print ("Allowed")
                elif sourceIP in blackListedIP:
                        if(blackListedIP.get(sourceIP) == destinationIP):
                                print "Refused"
                else:
                        if isBlackList(sourceIP, destinationIP):
							if sourceIP in blackListedIP:
								if destinationIP not in blackListedIP[sourceIP]:
									blackListedIP[sourceIP].append(destinationIP)
									print "You are Blacklisted"
								else:
									print "USELESSS"
							else:
								blackListedIP[sourceIP] = [destinationIP]
									#add_rule(sourceIP,destinationIP)       
                        else:
                                allowedIP[sourceIP]= [destinationIP]
                                print "You are Allowed"
                        # fileInput.write(sourceIP] + "  " + dataSplit[1])


        print ("BLACK LIST $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        count = 0;

        for iter in blackListedIP:
            count += 1
            print iter + " "  + str(blackListedIP[iter]) + "  " + str(count)
            print str(fileBlackListedIP) + " IN GET DATA METHOD"
            if iter not in fileBlackListedIP:

                resAndCategory = getDevName(iter)
		if resAndCategory != None:
                	fileOutput.write(iter + " " + str(blackListedIP[iter]) + str(resAndCategory)  +'\n')
                	fileBlackListedIP.append(iter + " " + str(blackListedIP[iter]) + str(resAndCategory))
                	fileOutput.flush()
		else:
			fileOutput.write(iter + " " + str(blackListedIP[iter]) + " None None" +'\n')
                        fileBlackListedIP.append(iter + " " + str(blackListedIP[iter]) + " None None" + '\n')
                        fileOutput.flush()

        print (" WHITE LIST $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        count = 0;
        for iter in allowedIP:
                count+=1
                print iter + " " + str(count)

getNextData(0)
counter = 0;
while 1:
        time.sleep(5)
        counter += 50
        getNextData(counter)
        print str(fileBlackListedIP) + " IN INFINITE LOOP"
        print ("IN WHILE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
