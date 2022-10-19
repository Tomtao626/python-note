###1.使用文件拖动

  yum install lrzsz



### 2.安装python3

```
https://www.cnblogs.com/NanZhiHan/p/11003229.html
#解压
tar -zxvf Python-3.8.10.tar

#进入解压后的目录，依次执行下面命令进行手动编译
./configure prefix=/usr/local/python3
make && make install

#将原来的链接备份
mv /usr/bin/python /usr/bin/python.bak

#添加python3的软链接
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python

#测试是否安装成功了
python -V

vi /usr/bin/yum
把#! /usr/bin/python修改为#! /usr/bin/python2

vi /usr/libexec/urlgrabber-ext-down
把#! /usr/bin/python 修改为#! /usr/bin/python2


```



### 3.安装crawlab

```
用docker下载crawlab镜像：

docker pull tikazyq/crawlab:latest
----------------------------------------------------------
安装 docker-compose：
‘’‘’‘’‘’‘’‘’‘’‘’‘方法一’‘’‘’‘’‘’‘’‘’‘’
pip3 install docker-compose

‘’‘’‘’‘’‘’‘’‘’‘’‘方法二’‘’‘’‘’‘’‘’‘’‘’
###### https://blog.csdn.net/weixin_31951989/article/details/113668995
sudo yum -y install curl
# Linux机器上下载最新的Compose
curl -s https://api.github.com/repos/docker/compose/releases/latest  | grep browser_download_url  | grep docker-compose-Linux-x86_64  | cut -d '"' -f 4  | wget -qi -

# 使二进制文件可执行
chmod +x docker-compose-Linux-x86_64
# 移动文件到相关目录
sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
docker-compose version
docker-compose ps
---------------------------------------------------------------------------------
#启动crawlab:
#需要先找到docker-compose.yml文件所在文件夹
docker-compose up  

```

### 4.adb

```
安卓目录：/storage/emulated/0/Android/data/top.niunaijun.blackdexa32/dump/com.mysteel.android.steelphone

# 安卓设备列表
adb devices
adb devices 显示device unauthorized
adb kill-server
adb start-server
# 进入安卓shell
adb shell
# 安卓日志
adb logcat
adb logcat -s keyword
#把文件推送进安卓设备
adb push
#打印AndroidManifest.xml
#adb shell dumpsys activity top
#adb shell dumpsys package packagename
adb install XXX.apk
adb uninstall packagename
#拉取安卓文件到本地
adb pull android-path local-path
#推送本地文件到安卓
adb push local-path android-path


adb push frida-server-12.4.0-android-arm /data/local/tmp/frida-server
adb shell
su
cd /data/local/tmp
chmod 777 frida-server
./frida-server

windows运行 端口转发到PC
 adb forward tcp:27043 tcp:27043
 adb forward tcp:27042 tcp:27042
 frida-ps -U 
```

