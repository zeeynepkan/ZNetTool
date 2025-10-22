import socket
import threading
import sys
import time

# General Settings
HOST = 'localhost'
PORT = 5000
LOG_FILE = "chat_log.txt"



# Auxiliary Functions
def log_message(message):
    """Write messages to both the screen and the file."""
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")



# SERVER SIDE
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    log_message(f"[SERVER] Chat server started on {HOST}:{PORT}")

    clients = []

    def broadcast(message, sender_socket=None):
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    clients.remove(client)

    def handle_client(client_socket, addr):
        log_message(f"[SERVER] {addr} connected.")
        while True:
            try:
                msg = client_socket.recv(1024).decode('utf-8')
                if not msg:
                    break
                formatted_msg = f"[{addr[0]}]: {msg}"
                log_message(formatted_msg)
                broadcast(formatted_msg, client_socket)
            except:
                break
        log_message(f"[SERVER] {addr} disconnected.")
        clients.remove(client_socket)
        client_socket.close()

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()


# CLIENT SIDE
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connected to the server. Start the server before.")
        sys.exit()

    print(f"[CLIENT] Connected to {HOST}:{PORT}")
    name = input("User name: ")

    def receive_messages():
        while True:
            try:
                msg = client_socket.recv(1024).decode('utf-8')
                if not msg:
                    print("[CLIENT] Server disconnected.")
                    break
                log_message(msg)
            except:
                break

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        msg = input()
        if msg.lower() in ["exit", "quit"]:
            client_socket.close()
            break
        timestamp = time.strftime("%H:%M:%S")
        message = f"{name} ({timestamp}): {msg}"
        client_socket.send(message.encode('utf-8'))



# MAIN MODULE
if __name__ == "__main__":
    mode = input("Do you want to start as server (s) or client (c)? (s/c): ").lower()
    if mode == "s":
        run_server()
    elif mode == "c":
        run_client()
    else:
        print("Invalid input. Write 's' or 'c'.")
