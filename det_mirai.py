from scapy.all import *
from lib.model import Flow, Packet

PACKETS = []
FLOWS = []
print "[*] program start"
pcap = rdpcap("1.pcap")[TCP]
print "[*] read complete"
count = 0
for p in pcap:
    if p.dport == 23:
        PACKETS.append(Packet(p, count))
        count += 1
print len(PACKETS)
count = 0
for p in PACKETS:
    for f in FLOWS:
        if f.ip_src == p.ip_src and f.ip_dst == p.ip_dst:
            f.add_packet(p)
            break
    else:
        flow = Flow(count, p)
        count += 1
        flow.add_packet(p)
        FLOWS.append(flow)
print "Flow  complete"
for f in FLOWS:
    for i in xrange(len(f.packets)):
        if not f.packets[i].raw.find("system") and not f.packets[i-2].raw.find("enable"):  # add more finger print like "mirai"
            print f.packets[i].raw, f.packets[i-2].raw
            print f.ip_src + "     " + f.ip_dst
            print "-------------------------------------------------"
            break