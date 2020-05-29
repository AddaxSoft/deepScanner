import xml.etree.ElementTree as ET
import os, sys, subprocess

#sanity check on file path in args
if len(sys.argv) < 2:
    print "[!] please feed in results.xml file from nmap scans"
    sys.exit(-1)

#another sanity check on file existence
file = sys.argv[1]
if not os.path.exists(file):
    print "[!] nmap xml file doesn't exists"
    sys.exit(-1)

#parse XML
tree = ET.parse(file)
root = tree.getroot()

hosts={}; port_str = ''; port_list=[]
for host in root.findall('host'):
    for ip in host.findall("./address"):
        ip_str = ip.get('addr')        
    for port in host.findall("./ports/port"):
        port_str = port.get('portid')
        port_list.append(port_str)
    hosts[ip_str] = port_list
    port_list = []

#if no hosts to scan quit...
if not len(hosts):
    print "[+] no hosts to scan. Quiting..."
    sys.exit(0)

#define scan type here
cmd = 'nmap -v -O -sV -R --dns-servers 1.1.1.1 -Pn --script vuln {HOST} -p {PORTS} -oA ./deepscan/{HOST}/results --stats-every 30m'     
original_cmd = cmd
for host in hosts.hosts():
    #clear screen for next scan.
    os.system("cls||clear")
    
    #some variables to save host and ports
    ports = ','.join(map(str, hosts[host]))
    cmd = cmd.format(HOST=host, PORTS=ports)
    
    #create dirs to store results
    path = "./deepscan/{HOST}/".format(HOST=host)
    if not os.path.exists(path):
        os.makedirs(path)
    
    #executing nmap via subprocess and print output to stdout
    print "starting a deeper scan for: %s:%s" %(host, ports)
    process = subprocess.Popen(cmd, shell=True, stdout=sys.stdout); process.wait()
    print "[+] nmap finished a deep scan for %s with exit code: %i" %(host,process.returncode)
        
    #reset cmd for next scan
    cmd = original_cmd

print "[+] All done. Hasta la vista baby. 😘"]
