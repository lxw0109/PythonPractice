#!/usr/bin/python
#coding:utf-8
#如果想有中文注释就必须得有上面的语句
#File: client.py
#Author: lxw
#Time: 2014-03-27
#Usage: Server.

import socket
import threading
 
#［不好使，在下面的sendall等函数中引用到才能好使］处理中文数据用的
#encoding = "GBK"  #"GBK"
 
# 服务器端，应该不需要太多的输出，尽量少用print
def HKServer(client, addr):
    #client: 客户socket;    addr: 客户address
 
    # 通知已有的每个客户，有新的成员加入
    for c in clients:
        if c != client:
            #c.send(bytes("[%s]加入\r\n" % addr[1], encoding))
            c.sendall('Welcome, {0} !'.format(addr[1]))
            
    # 接受客户端数据
    while True:        
        data = client.recv(1024)        
        if data.strip().lower() == 'exit':
            break
        '''
        # NOTE: 'FILE:' should not be dealed with here, the server's job is just to send this information.
        if data.strip().startswith('FILE:'):
            filename = data.strip()[5:]
        '''
        
        # data == FILE:1.jpg????1kExif
        if data.strip().startswith('FILE:'):
            #raw_input()
            #print 'YES: SERVER: data[:30] is ' + data[:30]
            #if data.strip().startswith('FILE:'):
            #    pass
            
            # NOTE: Here, while data is OK, but in client.py while content is not OK. Because [:] is not used here, data will never be ''.
            stopFlag = False
            while data:                
                for c in clients:
                    #c.send(bytes("[%s]:%s\r\n" % (addr[1], say.decode(encoding)), encoding))
                    if c != client:     # 自己的就不用发了
                        c.sendall(data)
                if not stopFlag:
                    data = client.recv(4096)
                else:
                    break
                if '__ENDFILEFLAG__' in data:
                    # data is not changed in replace method
                    if not data.replace('__ENDFILEFLAG__', ''):
                        break;
                    else:
                        stopFlag = True
                        
            print 'SERVER RECEIVING FINISHED.'
        else:
            #print 'NO: SERVER: data[:30] is ' + data[:30]
            # 把客户端发来的内容发给所有的客户端
            for c in clients:
                #c.send(bytes("[%s]:%s\r\n" % (addr[1], say.decode(encoding)), encoding))
                if c != client:     # 自己的就不用发了
                    c.sendall('{0}:\t{1}'.format(addr[1], data))
     
    # 客户离开后，从客户列表中移队当前客户，关闭socket连接
    clients.remove(client)
    client.close()
 
    # 通知已有的每个客户，有成员离开
    for c in clients:
        if c != client:
            #c.send(bytes("[%s]离开\r\n" % addr[1], encoding))
            c.sendall('Goodbye, {0} !'.format(addr[1]))

if __name__ == '__main__':
    # 客户端列表
    clients = []
     
    # 设置IP地址与端口
    HOST = ''
    PORT = 10086
     
    # 初始化socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # reuse the port immediately
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定IP地址与端口
    s.bind((HOST, PORT))
     
    # 开始监听
    s.listen(1)
     
    # 循环等待
    while True:
        # 接受客户
        client, addr = s.accept()
        # address =  ('127.0.0.1', 39990)    # tuple
     
        # 启动新的进程与客户通信
        thread = threading.Thread(target = HKServer, args = (client, addr))
        thread.start()
     
        # 记录新的客户
        clients.append(client)
