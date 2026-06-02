#########################
#    for studies only   #
#########################

from queue import Queue
from socket import AF_INET, gethostbyname, socket, SOCK_STREAM
import threading
import sys


def tcp_test(port: int, targetIP: str) -> None: # function that establishes a tcp connection w/ a specific port on the IP address.
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(1) # timeout for good practices
        result = sock.connect_ex((targetIP, port))
        if result == 0:
            print(f"-------- Opened port found: {port}")


def worker(target_ip: str, queue: Queue) -> None: # multi-threading
    while not queue.empty():
        port = queue.get()
        tcp_test(port, target_ip)
        queue.task_done()

def main(host: str, start_port: int, end_port:int) -> None:
    try:
       targetIP = gethostbyname(host)
    except Exception as e:
       print(f"-------- Error at finding the host: {e}")
       return
    
    print(f"\n-------- Initiating scanning on {targetIP} on range {start_port} - {end_port}")

    queue = Queue()
    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(100):
        t = threading.Thread(target=worker, args=(targetIP, queue,))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    host = input("-------- Inform the host IP: ")
    ports = (input("-------- Inform the range you wanna scan: "))

    try:
        ports_clear = ports.replace(" ", "")
        start_port, end_port = map(int, ports_clear.split('-'))

        main(host, start_port, end_port)
    except ValueError:
        print("\n -------- fuuu man error ma bad :( --------)")
        sys.exit()
    except KeyboardInterrupt:
        print("\n -------- scanning process cancelled --------")