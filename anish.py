import paramiko
from datetime import *

date = datetime.now().strftime('%d-%m-%Y')
cmd = '/opt/NetScout/rtm/bin/localconsole <11'
_username = 'root'
_password = 'netscout'

def workon(host):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		print("creating connection")
		ssh.connect(host, username=username, password=password,timeout=3)
		print("connected")
		stdin, stdout, stderr = ssh.exec_command(cmd)
		s = stdout.readlines()
		print(s)
	except Exception as e:
		with open(r'C:\Users\anisha\Desktop\Python\log.txt','a') as fw:
			fw.write(date + ':\t' + host + '\t' + str(e) + '\n')



	

def main():
	# IP addrss of IS here
	f = open(r'C:\Users\anisha\Desktop\Python\ipadd.txt','r')
	ip = f.read().split('\n')
	for host in ip:
		workon(host)


	

if __name__ == '__main__': 
	main()
	username = nikhil