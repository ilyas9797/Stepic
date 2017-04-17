sudo unlink /etc/nginx/sites-enabled/default
sudo ﻿ln -s /home/box/web/etc/nginx1.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -b 127.0.0.1:8080 hello:app
