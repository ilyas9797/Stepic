sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/default /home/box/web/etc/nginx1.conf 
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello:app
