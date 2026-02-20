##### REFERENCE FOR 

import ipaddress
import time

start_time = time.time() 

def process_cidr_input():
    """
    Prompts the user for a CIDR input and processes it using the ipaddress module.
    """
    while True:
        cidr_input = input("Please enter a CIDR network (e.g., 192.168.1.0/24): ")
        try:
            # Create a network object (IPv4Network or IPv6Network)
            network = ipaddress.ip_network(cidr_input)
            print(f"Successfully parsed network: {network}")
            print(f"Network address: {network.network_address}")
            print(f"Netmask: {network.netmask}")
            print(f"Prefix length: {network.prefixlen}")
            print(f"Number of addresses: {network.num_addresses}")
            break  # Exit loop if input is valid

        except ValueError as e:
            print(f"Error: Invalid CIDR input. {e}")
            print("Please try again with a valid CIDR notation.")

if __name__ == "__main__":
    process_cidr_input()

#### REFERENCE for the time part  ##################

import time
import socket # Example: using socket for a basic connection

TARGET_IP = '8.8.8.8' # Example IP (Google's DNS server)
TARGET_PORT = 53      # Example port

start_time = time.time() # Record the start time

try:
    # Your code that interacts with the IP address goes here
    # Example: a simple TCP connection attempt
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5) # Set a timeout
        s.connect((TARGET_IP, TARGET_PORT))
        print(f"Successfully connected to {TARGET_IP}:{TARGET_PORT}")
        # Further operations if needed...

except socket.error as e:
    print(f"Error connecting: {e}")

finally:
    end_time = time.time() # Record the end time
    duration = end_time - start_time
    print(f"Response time (connection attempt): {duration:.4f} seconds")
