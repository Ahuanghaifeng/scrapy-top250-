#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 25684                # 设置端口好

s.connect(('192.168.150.17',25684))
print s.recv(1024)
s.close()