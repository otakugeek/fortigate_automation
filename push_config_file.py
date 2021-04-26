import paramiko
import time

ip_address = "192.168.0.1"
username = "admin"
password = "admin"
restore_config_name="backup_192.168.0.1v2"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print ("Successfully connected to", ip_address)

remote_connection = ssh_client.invoke_shell()

restore_config=open(restore_config_name, "r")
content = restore_config.read().split("\n")
#print(content)
restore_config.close()


for command in content:
	remote_connection.send(command+"\n")


ssh_client.close()
