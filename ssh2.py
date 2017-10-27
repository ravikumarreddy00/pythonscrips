#!/usr/bin/python
import paramiko
offending = [">"]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn=ssh.connect('192.168.174.149', username='root', password='redhat', timeout=4)
stdin, stdout, stderr = ssh.exec_command('cat /etc/redhat-release')
print stdout.read()
