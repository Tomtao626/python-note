## docker创建/构建镜像
> + 比如项目目录为DockerTest，在该目录下执行`docker build . -t=docker-test:latest`
> + `-t` 指定名称及版本号`docker-test:latest`
> + `.` 构建内容为当前上下文目录

## 查看镜像
> + `docker images`

## 创建并启动容器
> + `sudo docker run -d -p 8000:80 docker-test:latest`
> + `-d` 后台守护模式
> + `-p` 指定容器与宿主机端口映射

## 查看docker内程序进程
> + `docker ps -a`

## 更优雅的启动容器，使用docker-compose
> + 编写docker-compose.yaml文件
```yaml
version: "2"
services:
    docker-test:
        image: docker-test:latest
        build: .
        container_name: docker-test
        restart: always
        ports:
            - "8000:80"
```

### 控制台执行命令
> + `docker-compose up -d` 启动容器
> + `docker ps` 验证容器docker-test是否启动

### 说明
> + version：docker-compose的版本
> + services：需要管理的服务
> + flask_test：FlaskApp服务名称
> + image：FlaskApp服务镜像来源
> + build：如果镜像不存在，当前位置构建镜像。存在则跳过
> + container_name：启动的容器名称
> + restart：容器启动属性， always一直重启
> + ports：容器与宿主机的端口映射