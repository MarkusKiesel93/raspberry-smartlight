# Setup:

## Python Requirements:
pip3 install -r ./requirements.txt

## Nginx:
sudo apt install nginx
sudo cp ./setup/nginx_site /etc/nginx/sites-available/smart_light
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/smart_light /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx start (or restart: sudo systemctl restart nginx.service)

## Smart Light Api:
sudo cp setup/smart_light.service /etc/systemd/system/
sudo systemctl start smart_light.service
get status: systemctl status smart_light.service

## Set coorect time zone:
sudo timedatectl set-timezone Europe/Vienna

## Find out pin layout in case of changes
use command: pinout
