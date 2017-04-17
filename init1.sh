sudo unlink /etc/nginx/sites-available/default
sudo ln -s /home/box/web/etc/nginx1.conf /etc/nginx/sites-available/default
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello:app
