#!/usr/bin/python
import paramiko
hostname = '192.168.174.149'
username = 'root'
password ='redhat'
def run_cmd(cmd):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname = hostname,username = username, password = password)
  stdin,stdout,stderr = ssh.exec_command(cmd)
  cmd_out = stdout.readlines()
  ssh.close()
  print stdout.readlines()
  return cmd_out
print run_cmd(cmd ='cat /etc/passwd')
  
