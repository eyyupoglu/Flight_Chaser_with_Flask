# Flight_Chaser_with_Flask
Flight ticket prices scraping and maintaining application with Flask 

# Server Setup Apache WSGI
1)
Clone the project
==================
#cd /usr/share
#sudo git clone https://github.com/sajuptpm/reg-service.git openstack_horizon_reg_service
#cd openstack_horizon_reg_service

2)
Create Virtualenv
====================
#sudo virtualenv venv
#source venv/bin/activate
#sudo pip install -r requirements.txt

3)
Create wsgi file
==================
#sudo mkdir wsgi
#cd wsgi
#sudo vim flask.wsgi
import os
import sys

##Virtualenv Settings
activate_this = '/usr/share/openstack_horizon_reg_service/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

##Add this file path to sys.path in order to import app
sys.path.append('/usr/share/openstack_horizon_reg_service/')

##Create appilcation for our app
from openstack_horizon_reg_service.run import app as application

4)
Apache Settings
=================
#cd /etc/apache2/conf-enabled
#sudo vim openstack-horizon-reg-service.conf 

WSGIScriptAlias /horizonreg /usr/share/openstack_horizon_reg_service/wsgi/flask.wsgi
WSGIScriptReloading On
 
Directory /usr/share/openstack_horizon_reg_service/wsgi>
  Order allow,deny
  Allow from all
Directory>

4a)
vim /etc/apache2/apache2.conf
#Include generic snippets of statements. 
#Following line should be there
IncludeOptional conf-enabled/*.conf

5)
Restart apache
===============
#sudo service apache2 restart

6)
http://127.0.0.1/horizonreg/users/123

- Checking the servers listening port 
"sudo netstat -tulpn | grep :80"

Restart apache
in order to see which user the apache is being run by 
ps aux | egrep '(apache|httpd)'

3-in order to see permissions of files under the directory
ls -l on /var/www/html/FlaskApp/FlaskApp

4-in order to change the "owner" of the files
chown root:root user_data.txt

5-in order to give permission
chmod -R 777 /var/www/html/FlaskApp/FlaskApp/__init__.py

NOTE: 
4: read
2: write
1: execute
0: no permission

you simply add these values and give permission to the user class etc.
