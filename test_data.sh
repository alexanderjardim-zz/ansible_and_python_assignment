#!/bin/bash

SERV_HOST="http://localhost:5000"

echo "As Admin create new Role Alpha"
curl -o /dev/null -H 'Authorization:hard_admin@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"name":"Alpha"}' $SERV_HOST/role

echo "As Admin create user Bob"
curl -o /dev/null -H 'Authorization:hard_admin@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"Bob@sanders.com"}' $SERV_HOST/user

echo "As Admin create user Lola"
curl -o /dev/null -H 'Authorization:hard_admin@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"lola@sysdamin.com"}' $SERV_HOST/user

echo "As Admin create service site1.com and Bob is the owner"
curl -o /dev/null -H 'Authorization:hard_admin@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"name": "site1.com","region": "nyc3","size": "512mb","image": "ubuntu-14-04-x64","ssh_keys": null,"backups": false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null, "tags": ["frontend"], "owner_login": "Bob@sanders.com" }' $SERV_HOST/service

echo "As Admin gives site1.com service ownership to Lola"
curl -o /dev/null -H 'Authorization:hard_admin@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -XPUT -d '{"owner_login": "lola@sysdamin.com"}' $SERV_HOST/service/1

echo "As Common User create user Bob"
curl -o /dev/null -H 'Authorization:hard_john@doe.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"Bob@sanders.com"}' $SERV_HOST/user

echo "As Common User create user Lola"
curl -o /dev/null -H 'Authorization:hard_john@doe.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"login":"lola@sysdamin.com"}' $SERV_HOST/user

echo "As Common User create service site1.com and Bob is the owner"
curl -o /dev/null -H 'Authorization:hard_john@doe.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"name": "site1.com","region": "nyc3","size": "512mb","image": "ubuntu-14-04-x64","ssh_keys": null,"backups": false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null, "tags": ["frontend"], "owner_login": "Bob@sanders.com" }' $SERV_HOST/service

echo "As Common User create service site2.com"
curl -o /dev/null -H 'Authorization:hard_john@doe.com' -H 'Content-type: application/json' -w "%{http_code}\n" -d '{"name": "Site3.com","region": "nyc2","size": "1024mb","image": "ubuntu-14-04-x64","ssh_keys": null,"backups": false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null, "tags": ["frontend"] }' $SERV_HOST/service

echo "As Common User gives site1.com service ownership to Lola"
curl -o /dev/null -H 'Authorization:hard_john@doe.com' -H 'Content-type: application/json' -w "%{http_code}\n" -XPUT -d '{"owner_login": "lola@sysdamin.com"}' $SERV_HOST/service/1

echo "As Bot search for services that match site*"
curl -o /dev/null -H 'Authorization:hard_bot@123.com' -w "%{http_code}\n" "$SERV_HOST/service/?search=site"

echo "As Bot delete service site1.com"
curl -o /dev/null -H 'Authorization:hard_bot@123.com' -H 'Content-type: application/json' -w "%{http_code}\n" -XDELETE $SERV_HOST/service/1
