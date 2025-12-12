import socket
import threading
from queue import Queue

# --------------------------
# CONFIGURATION
# --------------------------

target = input("Enter target IP: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))
print(f"\nStarting advanced scan on {target}...\n")

# Queue to store port numbers for threads
port_queue = Queue()

# To store open ports & their banners
open_ports = {}


# --------------------------
# FUNCTION: GRAB BANNER
# --------------------------
def grab_banner(sock):
    """
    Attempts to read service banner from an open port.
    Many services send a welcome message on connect.
    """
    try:
        sock.settimeout(1)
        banner = sock.recv(1024)
        return banner.decode().strip()
    except:
        return None


# --------------------------
# FUNCTION: SCAN FUNCTION
# --------------------------
def scan_port(port):
    """
    Attempts TCP connection to a port.
    If successful, grabs banner and saves results.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:  # Port open
            banner = grab_banner(sock)
            if banner:
                open_ports[port] = banner
                print(f"Port {port} OPEN | Banner: {banner}")
            else:
                open_ports[port] = "No banner"
                print(f"Port {port} OPEN")
        sock.close()

    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        exit()
    except:
        pass  # ignore errors to keep scanner running


# --------------------------
# THREAD WORKER FUNCTION
# --------------------------
def worker():
    """
    Each thread picks ports from queue and scans them.
    """
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(port)
        port_queue.task_done()


# --------------------------
# MAIN THREAD SETUP
# --------------------------

# Fill queue with port numbers
for p in range(start_port, end_port + 1):
    port_queue.put(p)

# Create and start threads
thread_count = 50  # Adjust for speed
threads = []

for _ in range(thread_count):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# --------------------------
# FINAL OUTPUT
# --------------------------

print("\nScan complete.")
print("Open Ports Found:")
for port, banner in open_ports.items():
    print(f"Port {port} : {banner}")
