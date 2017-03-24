# -*- coding: utf-8 -*-
"""

dnf install tor
编辑 /etc/tor/torrc，去掉下面的注释

ControlPort 9051
HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
如果想设置新的密码

tor --hash-password mypassword
启动tor

systemctl start tor
查看9050和9051端口是否开启

[root@the5 py]# netstat -tunlp | grep 9050
tcp        0      0 127.0.0.1:9050          0.0.0.0:*               LISTEN      6919/tor
[root@the5 py]# netstat -tunlp | grep 9051
tcp        0      0 127.0.0.1:9051          0.0.0.0:*               LISTEN      6919/tor


"""

import getpass
import sys

import stem
import stem.connection

from stem.control import Controller

if __name__ == '__main__':
    try:
        controller = Controller.from_port()
    except stem.SocketError as exc:
        print("Unable to connect to tor on port 9051: %s" % exc)
        sys.exit(1)

    try:
        controller.authenticate()
    except stem.connection.MissingPassword:
        pw = getpass.getpass("Controller password: ")

    try:
        controller.authenticate(password = pw)
    except stem.connection.PasswordAuthFailed:
        print("Unable to authenticate, password is incorrect")
        sys.exit(1)
    except stem.connection.AuthenticationFailure as exc:
        print("Unable to authenticate: %s" % exc)
        sys.exit(1)

    print("Tor is running version %s" % controller.get_version())
    controller.close()
