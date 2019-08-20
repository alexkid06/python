import paramiko
#import threading

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("10.0.0.9", username="root", password="toor")
chan = client.get_transport().open_session()
chan.send("connected")
print(chan.recv(1024))
client.close()
