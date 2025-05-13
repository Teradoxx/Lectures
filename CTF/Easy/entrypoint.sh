#!/bin/bash

# Start SSH
service ssh start

# Ensure MariaDB socket directory exists
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

# Start Apache
service apache2 start

# Start MariaDB
service mariadb start

# Prevent container from exiting by keeping SSH in the foreground
exec /usr/sbin/sshd -D
