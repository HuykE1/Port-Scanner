import socket
import threading
import pyfiglet
import queue

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

q = queue.Queue()

getIP = input("Enter a remote host to scan: ")
IPgot = socket.gethostbyname(getIP)

print("_" * 70)
print("Scanning, please wait")
print("_" * 70)


for i in range(1, 1001):
    q.put(i)


def scan():
     while not q.empty():
         port = q.get()
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
             try:
                 s.connect((IPgot, port))
                 print(f'port {port} is Open')
             except: 
                    pass
             q.task_done()

for i in range(1001):
    t = threading.Thread(target= scan, daemon=False)
    t.start()

q.join()
print('Scan complete')
