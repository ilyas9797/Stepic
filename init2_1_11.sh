sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx2_1_11.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn2_1_11.conf ask.wsgi:application

