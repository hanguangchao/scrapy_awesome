# -*- coding: utf-8 -*-
#
import time
import socket
import socks
import requests
from stem import Signal
from stem.control import Controller

controller = Controller.from_port(port=9051)

def connectTor():
    print("connectTor")
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renew_tor():
    print("renew_tor")
    pw = 'mypassword'
    controller.authenticate(password = pw)
    controller.signal(Signal.NEWNYM)

def showmyip():
    print("showmyip")
    r = requests.get('http://icanhazip.com/')
    ip_address = r.text.strip()
    print(ip_address)



showmyip()
renew_tor()
connectTor()
showmyip()

# for i in range(10):
#     renew_tor()
#     connectTor()
#     showmyip()
#     time.sleep(10)
