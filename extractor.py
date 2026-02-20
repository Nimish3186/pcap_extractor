import re
import sys

from scapy.all import *

if len(sys.argv)!=2:
    print("incorrect usage")
    sys.exit(1)

file=sys.argv[1]
packets = rdpcap(file)

'''for packet in packets:
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")

        if "POST" in payload or "password" in payload:
            print("\n[Possible Credential Found]")
            print(payload)'''

#print("Total packets :" , len(packets))
keywords = ["password", "username", "login", "Authorization", "Cookie"]

for packet in packets:
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")

        for word in keywords:
            if word in payload:
                with open("report.txt","a") as f:
                    
                    f.write("\n[Sensitive Data Detected]")
                    #f.write("Keyword:", word)
                    f.writelines(payload)
                #print(payload)

