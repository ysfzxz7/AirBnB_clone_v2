#!/usr/bin/env bash
# Script that configs a server with multiple settings.

# update and install the nginx if not exists:
sudo apt-get update
sudo apt-get install nginx -y
echo "installing nginx exits with status : $?"

# config the nginx firewall on HTTP:
sudo ufw allow 'Nginx HTTP'
echo "config firewall status : $?"

# create specific directories:
sudo mkdir -p /data/web_static/releases/test
echo "creating /data/web_static/releases/test status : $?"
sudo mkdir -p /data/web_static/shared
echo "creating /data/web_static/shared status : $?"

# create HTML file named index.html:
echo "Simple content :)." | sudo tee "/data/web_static/releases/test/index.html"
echo "creating the HTML file status : $?"

# remove the existing symbolic link if it exists:
if [ -L /data/web_static/current ]; then
    sudo rm -rf /data/web_static/current
    echo "removing symbolic link status : $?"
fi

# create the symbolic link:
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
echo "creating the symbolic link status : $?"

# change the ownership permissions:
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to serve the content:
config="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "/server_name _;/a\\$config\n" /etc/nginx/sites-available/default
echo "configuration status : $?"

# link the next files:
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo "link the default files status : $?"

# restart the nginx:
sudo service nginx restart
echo "restarting the nginx : $?"
