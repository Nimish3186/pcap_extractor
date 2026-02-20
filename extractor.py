from scapy.all import rdpcap
packets = rdpcap("test1.pcapng")
print("Total packets :" , len(packets))