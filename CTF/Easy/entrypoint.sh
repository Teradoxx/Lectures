#!/bin/bash

# Start SSH
service ssh start

# Ensure MariaDB socket directory exists
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

# Start Apache
service apache2 start

# Start MariaDB safely
service mariadb start

# Keep container running for SSH access
exec /usr/sbin/sshd -D
