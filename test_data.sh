#!/bin/bash

SERV_HOST="http://localhost:5000"

echo "Create user Bob"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"Bob@sanders.com"}' $SERV_HOST/user

echo "Create user Lola"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"lola@sysdamin.com"}' $SERV_HOST/user

echo "Create service site1.com and Bob is the owner"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"name": "site1.com","region": "nyc3","size": "512mb","image": "ubuntu-14-04-x64","ssh_keys": null,"backups": false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null, "tags": ["frontend"], "owner_login": "Bob@sanders.com" }' $SERV_HOST/service

echo "Gives site1.com service ownership to Lola"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -XPUT -d '{"owner_login": "lola@sysdamin.com"}' $SERV_HOST/service/1

echo "Search for services that match site*"
curl -o /dev/null -w "%{http_code}\n" "$SERV_HOST/service/?search=site"

echo "Delete service site1.com"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -XDELETE $SERV_HOST/service/1

echo "Delete user Bob"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -XDELETE $SERV_HOST/user/3

echo "Delete user Lola"
curl -o /dev/null -H 'Content-type: application/json' -w "%{http_code}\n" -XDELETE $SERV_HOST/user/4
