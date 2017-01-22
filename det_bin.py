from scapy.all import *


def main():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        msg = "Usage:\n  python pcapdata.py [pcap-file]\n" \
              "Example:\n  python pcapdata.py ../ca1_http.pcap"
        sys.exit(msg)

    pcap = rdpcap(sys.argv[1])[TCP]
    for p in pcap:
        lines = str(p).split("\n")
        for line in lines:
            if line[0:2] == "MZ" or line[1:4] == "ELF":
                print p['IP'].src + "   " + p['IP'].dst + "\n"
if __name__ == '__main__':
    main()