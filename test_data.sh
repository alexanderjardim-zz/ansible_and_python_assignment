#!/bin/bash

SERV_HOST="http://localhost:5000"

echo "Create user Bob"
curl -v -H 'Content-type: application/json' -XPOST -d '{"login":"Bob@sanders.com"}' $SERV_HOST/user

echo "Create service site1.com"
curl -v -H 'Content-type: application/json' -XPOST -d '{"name": "site1.com","region": "nyc3","size": "512mb","image": "ubuntu-14-04-x64","ssh_keys": null,"backups":
false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null,"tags": ["frontend"]}' $SERV_HOST/service

echo "Delete user Bob"
curl -v -H 'Content-type: application/json' -XDELETE $SERV_HOST/user/3

echo "Delete service site1.com"
curl -v -H 'Content-type: application/json' -XDELETE $SERV_HOST/service/1
