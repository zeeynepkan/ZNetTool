import socket
import psutil

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    network_interfaces = psutil.net_if_addrs()
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)
    print("Network interfaces: %s" % network_interfaces)


if __name__ == "__main__":
    print_machine_info()
