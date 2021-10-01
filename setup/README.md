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
sudo cp ./setup/smart_light_api /etc/init.d/
sudo chmod 755 smart_light_api
sudo update-rc.d smart_light_api defaults

## Set coorect time zone:
sudo timedatectl set-timezone Europe/Vienna

## Find out pin layout in case of changes
use command: pinout
