sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx2_1_11.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py migrate
gunicorn -c /home/box/web/etc/gunicorn2_1_11.conf ask.wsgi:application

