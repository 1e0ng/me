#Me
It's an internal SNS for employees of same company. Actually, we use this project in :quudouban as there are over 300 people who are not very familiar with each other very well.



#Dependency
mysql

MySQL-python

quixote 1.0

beansdb

redis

juggernaut

wand

#Run
create database me

mysql -ubear -Dme < db.sql

ln -s /home/user/me/static /tmp/me-static/static

sudo nginx -c /home/user/me/etc/nginx.conf

gunicorn -w 4 app:app -b 127.0.0.1:8000
