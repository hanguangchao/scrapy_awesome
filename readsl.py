# -*- coding: utf-8 -*-


import os
import requests
import time

g_adsl_account = {"name": "adsl",
                "username": "11010100128904",
                "password": "2itn5m"}

    
class Adsl(object):
    #==============================================================================
    # __init__ : name: adsl名称
    #==============================================================================
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]

        
    #==============================================================================
    # set_adsl : 修改adsl设置
    #==============================================================================
    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]

    
    #==============================================================================
    # connect : 宽带拨号
    #==============================================================================
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        # time.sleep(5)

        
    #==============================================================================
    # disconnect : 断开宽带连接
    #==============================================================================
    def disconnect(self):
        print "disconnect"
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        #time.sleep(5)

    
    #==============================================================================
    # reconnect : 重新进行拨号
    #==============================================================================
    def reconnect(self):
        print "reconnect"
        self.disconnect()
        self.connect()


if __name__ == '__main__':
    adsl = Adsl()
    print requests.get('http://ip.chinaz.com/getip.aspx').text
    adsl.disconnect()
    adsl.connect()
    print requests.get('http://ip.chinaz.com/getip.aspx').text  
