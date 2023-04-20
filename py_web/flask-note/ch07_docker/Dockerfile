FROM python:3
MAINTAINER "username<useremail>"
ENV PIPURL "https://pypi.tuna.tsinghua.edu.cn/simple"
WORKDIR /projects

COPY app.py app.py
RUN pip --no-cache-dir install -i $(PIPURL) --upgrade pip
RUN pip --no-cache-dir install  -i ${PIPURL} gunicorn==19.9.0
RUN pip --no-cache-dir install  -i ${PIPURL} flask==1.0.2
RUN pip --no-cache-dir install  -i ${PIPURL} gevent==1.4.0

CMD gunicon -c gun.conf app:app

#Dockerfile 文件是用于定义 Docker 镜像生成流程的配置文件，文件内容是一条条指令，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建；这些指令应用于基础镜像并最终创建一个新的镜像，可以认为用于快速创建自定义的Docker镜像。
#
#1.FORM
#指定基础镜像（必须有的指令，并且必须是第一条指令）
#
#2.MAINTAINER
#用于提供信息的指令，用于让作者提供本人的信息；不限制其出现的位置，但建议紧跟在FROM之后
#
#格式：
#
#MAINTAINER <name>
#3.ENV
#设置环境变量，可以在RUN之前使用，然后RUN命令时调用，容器启动时这些环境变量都会被指定
#
#格式：
#
#ENV <key> <value>  一次定义一个变量
#ENV <key>=<value> ...   一次可定义多个变量
#4.WORKDIR
#WORKDIR指令可以来指定工作目录（或者称为当前目录），以后各层的当前目录就被改为指定的目录，如果目录不存在，WORKDIR会建立目录
#
#格式：
#
#WORKDIR <工作目录路径>
#5.COPY
#格式：
#
#COPY <源路径>... <目标路径>
#COPY ["<源路径1>",... "<目标路径>"]
#COPY 指令将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置
#
#6.RUN
#用于执行命令行命令
#
#格式：
#
#RUN <命令>
#7.CMD
#类似于RUN指令，用于运行程序；但二者运行的时间点不同；CMD在docker run时运行，而非docker build