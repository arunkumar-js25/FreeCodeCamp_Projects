import nmap

nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"

scanner = nmap.PortScanner(nmap_search_path = nmap_path)
print('Start NMAP Scanner')

ip = input('Please enter your IP Address')
type(ip)

choice = input("""\nPlease select your Scan Option:
                    1) SYN ACK SCAN
                    2) UDP SCAN
                    3) Comprehensive SCAN\n""")

if(choice=='1'):
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: "+scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open Ports: ",scanner[ip]['tcp'.keys()])
elif(choice=='2'):
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')  #we can change the port limit and option to scan
    print(scanner.scaninfo())
    print("Ip Status: "+scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open Ports: ",scanner[ip]['udp'.keys()])
elif(choice=='3'):
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: "+scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open Ports: ",scanner[ip]['tcp'.keys()])
else:
    print("Please enter a valid choice")