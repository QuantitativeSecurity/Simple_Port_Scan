Simple Port Scanner

This program is a simple port scanner that attempts to connect to a range of ports on a specified IP address to identify which ports are open.
Dependencies

    Python 3.x
    socket library (Included with Python)

Usage

    Copy the code from the program and save it into a file named port_scanner.py.
    Replace the placeholder "X.X.X.X" with the target IP address you wish to scan.
    Execute the program by running the following command in your terminal:

bash

python port_scanner.py

Program Overview

The program performs the following steps:

    Importing Necessary Library:
    The socket library is imported for network communication.

    Defining Port Scan Function:
        port_scan(ip, port): This function tries to establish a TCP connection to the specified ip and port. If the connection is successful, it prints that the port is open.

    Setting Target IP:
    Replace the placeholder "X.X.X.X" with the IP address you want to scan.

    Scanning Ports:
    A loop iterates through the first 1023 ports, calling the port_scan function on each port.

    Checking Open Ports:
    If there are any open ports found, it prints the list of open ports. If no open ports are found, it prints a message indicating so.

Output

The program outputs the status of each port (open or closed) on the specified IP address. If any open ports are found, it prints a list of open ports; otherwise, it prints a message indicating no open ports were found.
