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
