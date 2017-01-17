from scapy.all import *
PACKETS = []
FLOWS = []


class Packet:
    def __init__(self, packet):
        self.ip_src = packet['IP'].src
        self.ip_dst = packet['IP'].dst
        self.port_src = packet['IP'].sport
        self.port_dst = packet['IP'].dport
        self.time = packet.time


class Flow:
    def __init__(self, packet):
        self.ip_src = packet.ip_src
        self.port_src = packet.port_src
        self.packets = [packet, ]
        self.dst = [[packet.ip_dst, [packet.port_dst]]]
        self.time = 0

    def cacl_time(self):
        if len(self.packets) == 1:
            self.time = 99999  # big number  unit   s
            return
        self.time = self.packets[-1].time - self.packets[0].time


def main():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        msg = "Usage:\n  python pcapdata.py [pcap-file]\n" \
              "Example:\n  python pcapdata.py ../ca1_http.pcap"
        sys.exit(msg)

    read_pcap(sys.argv[1])
    split_flow()
    print len(FLOWS)
    file = open("test.txt", 'w')

    for f in FLOWS:
        for d in f.dst:
            if len(d[1])/f.time > 6 or len(f.dst)/f.time > 6:
                file.write(str(len(d[1]) / f.time) + "  " + str(len(f.dst) / f.time) + "    ")
                file.write(str(f.ip_src) + "  " + str(f.port_src) + "  " + str(d[0]) + "\n")


def read_pcap(path):
    pcap = rdpcap(path)[TCP]
    print len(pcap)
    for p in pcap:
        PACKETS.append(Packet(p))

    print '[common] Total packets: %d' % len(PACKETS)


def split_flow():
    for p in PACKETS:
        for f in FLOWS:
            if f.ip_src == p.ip_src: #and f.port_src == p.port_src:
                f.packets.append(p)
                for d in f.dst:
                    if p.ip_dst == d[0] and p.port_dst not in d[1]:
                        d[1].append(p.port_dst)
                        break
                    elif p.ip_dst == d[0] and p.port_dst in d[1]:
                        break
                else:
                    dst = [p.ip_dst, [p.port_dst, ]]
                    f.dst.append(dst)
                break
        else:
            flow = Flow(p)
            if flow not in FLOWS:
                FLOWS.append(flow)
    for f in FLOWS:
        f.cacl_time()

if __name__ == '__main__':
    main()
