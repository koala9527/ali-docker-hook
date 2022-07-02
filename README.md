# ali-docker-hook
# 阿里云镜像服务触发器  基于Python Flask 框架的HTTP服务端


接收镜像服务自动构建后的触发器消息，处理阿里云自动打包镜像完成后通过触发器发送的tag信息，从而执行shell命令更新docker-compose 文件镜像tag名称，拉取镜像更新服务


注意要使用`chmod +x update.sh`给予执行权限

后期可以加上消息推送


## 阿里云镜像服务触发器配置：
![阿里云镜像服务触发器配置](https://github.com/koala9527/ali-docker-hook/blob/main/aliyun.png)

阿里云镜像服务文档参考：https://help.aliyun.com/document_detail/60949.html

## 部署服务器
python版本3.6+  
将app.run 放在有公网地址的机器某个目录下  
`pip install flask`  
`pip install gunicorn`  
使用gunicorn  部署flask http服务器 `gunicorn app:app -b 0.0.0.0:35555 -w 2 -D`

下图是直接在服务器`python run.app`打印的效果：
![consle](https://github.com/koala9527/ali-docker-hook/blob/main/console.png)

#### docker-compose demo参考：
```
 version: "3.5"
 
 services:
   my-applet:
     image: registry.cn-shenzhen.aliyuncs.com/******/******:1.0.2
     container_name: ******
     restart: always
     ports:
       - "9501:9501"
```
