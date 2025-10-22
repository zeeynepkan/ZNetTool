import socket
import struct
import pickle
import sys
import argparse
import time
import select

SERVER_HOST = 'localhost'

def log(msg):
    """Write both of screen and file."""
    print(msg)
    with open("socket_settings_log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# Common send / receive functions
def send(channel, *args):
    """Send the data with pickle."""
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    try:
        channel.send(size)
        channel.send(buffer)
    except socket.error as e:
        log(f"[ERROR] Send failed: {e}")


def receive(channel):
    """Receive data with pickle."""
    size_data = channel.recv(struct.calcsize("L"))
    try:
        size = socket.ntohl(struct.unpack("L", size_data)[0])
    except struct.error:
        return ''
    buf = b""
    while len(buf) < size:
        try:
            data = channel.recv(size - len(buf))
            if not data:
                break
            buf += data
        except socket.timeout:
            log("[TIMEOUT] Receive operation timed out.")
            break
        except BlockingIOError:
            log("[INFO] Non-blocking socket has no data yet.")
            break
    if buf:
        return pickle.loads(buf)[0]
    return ''

# Chat Server Class
class ChatServer:
    def __init__(self, port, timeout=5, blocking=True):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # *** SOCKET SETTINGS ***
        self.server.settimeout(timeout)  # connection timeout
        self.server.setblocking(blocking)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)

        log(f"[SERVER SETTINGS]")
        log(f"  Timeout: {timeout}s")
        log(f"  Blocking: {blocking}")
        log(f"  RECEIVE BUFFER: {self.server.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)} bytes")
        log(f"  SEND BUFFER: {self.server.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)} bytes")

        try:
            self.server.bind((SERVER_HOST, port))
            self.server.listen(5)
            log(f"[OK] Server listening on {SERVER_HOST}:{port}")
        except socket.error as e:
            log(f"[ERROR] Socket bind/listen failed: {e}")
            sys.exit(1)

        self.inputs = [self.server]
        self.outputs = []
        self.clientmap = {}

    def run(self):
        while True:
            try:
                readable, _, _ = select.select(self.inputs, [], [], 1)
            except select.error as e:
                log(f"[ERROR] Select failed: {e}")
                continue

            for s in readable:
                if s == self.server:
                    try:
                        client, address = self.server.accept()
                        log(f"[CONNECT] {address} connected.")
                        self.inputs.append(client)
                        self.clientmap[client] = address
                    except socket.timeout:
                        log("[TIMEOUT] No incoming connections.")
                    except BlockingIOError:
                        log("[INFO] Non-blocking accept found no client.")
                else:
                    data = receive(s)
                    if data:
                        msg = f"[{self.clientmap[s]}] {data}"
                        log(msg)
                        for c in self.inputs:
                            if c not in (self.server, s):
                                send(c, msg)
                    else:
                        log(f"[DISCONNECT] {self.clientmap.get(s, '?')} disconnected.")
                        s.close()
                        self.inputs.remove(s)
                        del self.clientmap[s]


# Chat Client Class
class ChatClient:
    def __init__(self, name, port, timeout=3, blocking=True):
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(timeout)
        self.sock.setblocking(blocking)

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2048)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

        log(f"[CLIENT SETTINGS]")
        log(f"  Timeout: {timeout}s")
        log(f"  Blocking: {blocking}")
        log(f"  RCVBUF: {self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)} bytes")
        log(f"  SNDBUF: {self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)} bytes")

        try:
            self.sock.connect((SERVER_HOST, port))
            log(f"[OK] Connected to {SERVER_HOST}:{port}")
        except socket.timeout:
            log("[ERROR] Connection attempt timed out.")
            sys.exit(1)
        except socket.error as e:
            log(f"[ERROR] Connection failed: {e}")
            sys.exit(1)

    def run(self):
        while True:
            try:
                msg = input("Message: ")
                send(self.sock, f"{self.name}: {msg}")
            except KeyboardInterrupt:
                log("[CLIENT] User interrupted.")
                self.sock.close()
                break
            except socket.error as e:
                log(f"[ERROR] {e}")
                break


# MAIN MODULE
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Error & Settings Module")
    parser.add_argument('--mode', choices=['server', 'client'], required=True)
    parser.add_argument('--port', type=int, default=5000)
    parser.add_argument('--name', default='client1')
    parser.add_argument('--timeout', type=float, default=3.0)
    parser.add_argument('--nonblock', action='store_true')

    args = parser.parse_args()
    blocking = not args.nonblock

    if args.mode == 'server':
        server = ChatServer(args.port, timeout=args.timeout, blocking=blocking)
        server.run()
    else:
        client = ChatClient(args.name, args.port, timeout=args.timeout, blocking=blocking)
        client.run()


 #py error_settings_module.py --mode=server --port=8800 --timeout=5 --nonblock
 #py error_settings_module.py --mode=client --port=8800 --timeout=5 --nonblock
