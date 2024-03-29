import socket           #importing all modules required for code
import threading
import pyfiglet
import queue

banner = pyfiglet.figlet_format("PORT SCANNER")         #Creating the banner title for the port scanner
print(banner)

q = queue.Queue()

getIP = input("Enter a remote host to scan: ")          #Allowing the user to input selected IP address
IPgot = socket.gethostbyname(getIP)         #Retrieving the inputted IP

print("_" * 70)         #Creating lines and showing process is starting
print("Scanning, please wait")
print("_" * 70)


for i in range(1, 1001):            #Putting elements into the queue
    q.put(i)


def scan():         #Function that carries out the scan by eliminating all treads
     while not q.empty():
         port = q.get()
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
             try:
                 s.connect((IPgot, port))
                 print(f'port {port} is Open')
             except: 
                    pass
             q.task_done()

for i in range(1001):           #Number of threads wished to use
    t = threading.Thread(target= scan, daemon=False)
    t.start()

q.join()            #Ensures all elements in the queue have their tasks done before ending the application
print('Scan complete')
