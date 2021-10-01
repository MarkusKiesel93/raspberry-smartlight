# Setup:

## Python Requirements:
pip3 install -r ./requirements.txt

## Nginx:
sudo apt install nginx
sudo rm /etc/nginx/conf.d/default.conf
sudo cp ./setup/nginx.conf /etc/nginx/conf.d/
sudo /etc/init.d/nginx start

## Smart Light Api:
sudo cp ./setup/smart_light_api /etc/init.d/
sudo chmod 755 smart_light_api
sudo update-rc.d smart_light_api defaults