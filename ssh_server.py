import socket
import paramiko
import threading
import sys

host_key = paramiko.RSAKey(filename=r"/root/Desktop/new.key")


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == "user") and (password == "pass"):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("ip_bind", port_bind))
    sock.listen(1) #number of connections#
    print('[+] Listening for connection ...')
    client, addr = sock.accept()
except Exception as e:
    print('[-] Listen/bind/accept failed: ' + str(e))
    sys.exit(1)
print('[+] Got a connection!')

try:
    t = paramiko.Transport(socket)
    try:
        t.load_server_moduli()
    except:
        print('[-] (Failed to load moduli -- gex will be unsupported.)')
        raise
    t.add_server_key(host_key)
    server = Server()

    try:
        t.start_server(server=server)
    except paramiko.SSHException as x:
        print("[-] SSH negotiation failed.")

        chan = t.accept(20)
        print("[+] Authenticated!")
        print(chan.recv(1024))
        chan.send("can see this")
except Exception as e:
    print('[-] Caught exception')
    try:
        t.close()
    except:
        pass
    sys.exit(1)
