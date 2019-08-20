import paramiko
#import threading

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("ip_bind", username="user", password="pass")
chan = client.get_transport().open_session()
chan.send("connected")
print(chan.recv(1024))
client.close()
