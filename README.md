Advanced Python Port Scanner

This project is a multi-threaded, banner-grabbing port scanner written in Python.
It is designed for fast scanning of TCP ports and identifying running services by capturing service banners.

This script demonstrates practical knowledge of:

Socket programming

Multi-threading

Banner grabbing

Queue-based thread management

Exception handling

Network troubleshooting

Basic cybersecurity concepts

Use this tool only on systems you are authorized to scan.

Features

Multi-threaded scanning (fast and efficient)

Configurable port ranges

Banner grabbing to identify services running on open ports

Thread pool for parallel scanning

Graceful error handling

Simple and readable code structure

How It Works

User provides:

Target IP address

Start port

End port

The program:

Fills a queue with ports

Launches 50 worker threads

Each thread picks a port and performs a TCP connection

If the port is open, the script attempts banner grabbing

Results are stored and displayed at the end

Requirements

Python 3.x

No external libraries required

Usage
Run the script:
python3 advanced_port_scanner.py

Example Input:
Enter target IP: 192.168.1.10
Start Port: 1
End Port: 1000

Example Output:
Port 22 OPEN | Banner: SSH-2.0-OpenSSH_8.2
Port 80 OPEN | Banner: HTTP/1.1 400 Bad Request
Port 443 OPEN
Scan complete.
Open Ports Found:
Port 22 : SSH-2.0-OpenSSH_8.2
Port 80 : HTTP/1.1 400 Bad Request
Port 443 : No banner
