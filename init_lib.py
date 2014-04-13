#coding=utf8

#windows & linux 下需要安装  python-setuptools

import platform

if(platform.system()=="Windows"):
    os.system("./windows_install_lib.bat") #没有调通，需要下载wget
else:
    os.system("./linux_install_lib.sh")

