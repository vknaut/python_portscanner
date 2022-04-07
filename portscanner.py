# Simple Portscanner using threading
import socket
import threading
import time
import datetime
import sys

def scan(remoteServerIP, port):
    try:   
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))         
        sock.close()
        with open("log.txt", "a") as log:
                log.write("Port " + str(port) + " is open\n")
    except Exception as e:
        print(e)
        pass
        

def main():
    print("Welcome to the port scanner!")
    print("Please enter the IP address you want to scan:")
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    print("Please enter the port range you want to scan (e.g. 1-100):")
    port_range = input()
    port_range = port_range.split("-")
    port_range = list(map(int, port_range))
    print("Scanning...")
    start_time = time.time()
    for port in range(port_range[0], port_range[1]):
        t = threading.Thread(target=scan, args=(remoteServerIP, port))
        t.start()
    end_time = time.time()
    print("Scan completed in", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
