import paramiko
import time

ipa="10.60.1.40"
username = "CCXAdmin"
password = input("Password: ")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ipa, username=username, password=password,timeout=120)
time.sleep(30)
command = "show version active"
stdin, stdout, stderr = client.exec_command(command)
output = stdout.read().decode()
print(output)
client.close()