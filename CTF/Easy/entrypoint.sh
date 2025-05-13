#!/bin/bash

service ssh start

# Ensure MariaDB socket directory exists
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

# Start Apache
service apache2 start

# Start MariaDB safely
service mariadb start

exec /usr/sbin/sshd -D
