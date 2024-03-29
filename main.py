import socket
import threading
import queue
import pyfiglet

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)


IP= '192.168.0.38'
q = queue.Queue()

for i in range(1, 1001):
    q.put(i)


def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
              s.connect((IP, port))
              print(f'port {port} is Open')
            except: 
                  pass
        q.task_done()
    

for i in range(30):
    t = threading.Thread(target= scan, daemon= True)
    t.start()

q.join()
print('Scan complete')
