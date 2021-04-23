import paramiko
import time

import re
ip_address = "192.168.0.1"
username = "admin"
password = "admin"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print ("Successfully connected to", ip_address)

remote_connection = ssh_client.invoke_shell()


remote_connection.send("show\n")

time.sleep(1)
output = remote_connection.recv(1000000000)

#print(output)
configs=re.split('\n',''.join(chr(i) for i in output)) #conversion en ascii et les splitter par lignes
delete=0;
for config in configs:
    if not "#config-version" in config:
        delete=delete+1
    else: 
        break


with open('backup_'+ip_address, 'w') as filehandle:
    for listitem in configs[delete:-2]:
        filehandle.write('%s\n' % listitem);


ssh_client.close()
