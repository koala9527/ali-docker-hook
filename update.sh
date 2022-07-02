#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cd /******/*******/*******/

sed "s/[0-9]\.[0-9]\.[0-9]/$1/" -i docker-compose.yml

rm -rf runtime/container/
echo -e "已删除缓存文件"
docker-compose up -d --force-recreate
sleep 1s
echo "服务已启动"
docker-compose logs -ft