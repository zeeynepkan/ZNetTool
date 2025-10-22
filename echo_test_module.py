import socket
import sys
import argparse

HOST = 'localhost'
DATA_PAYLOAD = 2048
BACKLOG = 5


def echo_server(port=8880):
    """A simple echo server"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (HOST, port)
    print(f"Starting up echo server on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)
    sock.listen(BACKLOG)

    while True:
        print("Waiting to receive message from client...")
        client, address = sock.accept()
        print(f"Connection from {address}")
        try:
            data = client.recv(DATA_PAYLOAD)
            if data:
                print(f"Data received: {data.decode('utf-8')}")
                client.sendall(data)
                print(f"Sent {len(data)} bytes back to {address}")
        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            client.close()
            print(f"Connection with {address} closed.\n")


def echo_client(port=8880):
    """A simple echo client"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, port)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")

    try:
        sock.connect(server_address)
        message = "This is my first socket programming and this will be echoed"
        print(f"Sending: {message}")
        sock.sendall(message.encode('utf-8'))

        received_data = b""
        while True:
            data = sock.recv(16)
            if not data:
                break
            received_data += data
            print(f"Received: {data}")

        received_message = received_data.decode('utf-8')
        if message == received_message:
            print("✅ Connection successful, data matches")
        else:
            print("❌ Connection failed, data does not match")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other exception: {e}")
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo Server/Client in one script")
    parser.add_argument('--mode', choices=['server', 'client'], required=True, help='Run as server or client')
    parser.add_argument('--port', type=int, default=8880, help='Port number (default: 8880)')
    args = parser.parse_args()

    if args.mode == 'server':
        echo_server(args.port)
    else:
        echo_client(args.port)
