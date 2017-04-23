mysql -u root -e "CREATE DATABASE ask;"
mysql -u root -e "CREATE USER user@localhost;"
mysql -u root -e "GRANT ALL ON ask.* TO 'user'@'localhost';"

