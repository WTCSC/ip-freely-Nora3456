import ipaddress
import socket
import time


def process_cidr_input():
    """Processes the cidr notation a uuser gave to make sure it is valid."""
    while True:
        cidr_input = input("Enter your CIDR notation: ")
        try:
            network = ipaddress.ip_network(cidr_input)
            return network
        except ValueError as e:
            print(f"Invalid CIDR: {e}")
            print("Try again.\n")


def scan_host(ip, port=80):
    """Shows how long the response/request took converting the time to miliseconds, and shows if the network is becoming smaller or larger (up or down)."""
    start_time = time.time()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((str(ip), port))

        duration = (time.time() - start_time) * 1000
        return "UP", f"{duration:.2f} ms"

    except socket.timeout:
        duration = (time.time() - start_time) * 1000
        return "DOWN", f"{duration:.2f} ms"

    except socket.error as e:
        duration = (time.time() - start_time) * 1000
        return "ERROR", f"{duration:.2f} ms"


if __name__ == "__main__":

    network = process_cidr_input()

    print(f"\nScanning network {network}...\n")

    up_count = 0
    down_count = 0
    error_count = 0
    total_hosts = 0

    try:
        for ip in network.hosts():
            total_hosts += 1

            status, response_time = scan_host(ip)

            if status == "UP":
                up_count += 1
            elif status == "DOWN":
                down_count += 1
            else:
                error_count += 1

            print(f"{str(ip):<15} - {status} ({response_time})")

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")

    finally:
        print("\nScan complete!:")
        print(f"Total hosts scanned: {total_hosts}")
        print(f"Active hosts (UP): {up_count}")
        print(f"Down hosts: {down_count}")
        print(f"Errors: {error_count}")