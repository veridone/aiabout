@echo off & color 09
mkdir D:\Download
CD D:\Download

set /p myAddr="https://pypi.python.org/packages/2.5/n/nltk/nltk-2.0.4.win32.exe#md5=1f906b2692dc8ef7a76d2d841ceaa6c3"
wget -c "%myAddr%"
pause
.\nltk-2.0.4.win32.exe

set /p myAddr="https://pypi.python.org/packages/2.6/P/PyYAML/PyYAML-3.11.win32-py2.6.exe#md5=83b0f47825feac2da99b75bfbd65a3ab"
pause
.\PyYAML-3.11.win32-py2.7.exe

close
