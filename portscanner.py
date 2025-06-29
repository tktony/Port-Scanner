import socket 
import threading
from queue import Queue

target = "192.168.0.1"  # Target IP (e.g., your router or localhost) — ONLY SCAN DEVICES YOU OWN OR HAVE PERMISSION FOR
queue = Queue()         # Queue to store ports to be scanned (FIFO structure)
open_ports = []         # List to store open ports found during scanning

# TCP Port Scanner Function
def port_scan (port):

    try:
        # 1. Create a TCP socket and pass parameters 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM = we are using TCP instead of UDP

        # 2. Try to connect to the target IP and port 
        sock.connect((target, port)) # Passing a tuple: 1.IP Address(Target) 2.Port

        # 3. Connection Success - Open Port
        return True
    
    except:
        # Or Conneection Failure - Closed Port
        return False
    
# print(port_scan(80)) # HTTP port returns True
# print(port_scan(443)) # HTTPS port returns False



''' Single-Threaded Port Scanning. ~5-10ports/sec '''
for port in range (1, 1024): # standartized ports that are reserved for HTTP, FTP, SSH, TelNet and so on
    result = port_scan(port)
    if result:
        print("Port {} is open!".format(port))
    else: 
        print("Port {} is closed!".format(port))



''' Multi-threading Port Scanning. ~500-2000 ports/sec'''
# Uses threads + queue to speed up scanning and avoid duplicate scanning

# 1. Queue all port numbers to be scanned
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# 2. Each thread runs this worker function to scan ports from the queue
def worker():
    while not queue.empty():                       # 1. As long as the Queue is not empty
        port = queue.get()                         # 2. Get the next item on the Queue
        if port_scan(port):                        # 3. Scanning 
            print("Port {} is open!".format(port))
            open_ports.append(port)                # 4. Adding the port to open_ports list
                                                   # 5. Closed ports are skipped for speed

# 3. Define port range and populate the queue        
port_list = range(1, 1024)
fill_queue(port_list)

# 4. Create and start multiple threads
thread_list = [] 

for t in range(500):                         # Adjust number of threads based on system capacity
    thread = threading.Thread(target=worker) # Refering to the worker as the target function (not actually calling it)
    thread_list.append(thread)               # Add each thread to the list for later management

for thread in thread_list:
    thread.start()                           # Starts the thread (runs worker function)

# 5. Wait for all threads to complete
for thread in thread_list:
    thread.join()                            # Ensures main program waits for thread to finish

# 8. Output the final list of open ports 
print("Open ports are: ", open_ports)       
