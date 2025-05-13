#!/bin/bash

# Set the number of users
X=5

# Generate a unique container name per session
USER_CONTAINER="ctf_$(uuidgen)"

# Create users inside the container
echo "Creating $X users..."
for i in $(seq 1 $X); do
    USER="user$i"
    PASS="password$i"
    echo "User: $USER | Password: $PASS"
done

# Start a new disposable container and keep it running
echo "Launching new container: $USER_CONTAINER"
docker run --rm -it --name "$USER_CONTAINER" -p 22:22 ctf_challenge /bin/sh -c "
    for i in \$(seq 1 $X); do
        useradd -m user\$i && echo user\$i:password\$i | chpasswd;
    done;
    service ssh start;
    exec /usr/sbin/sshd -D
"

# Keep the script running indefinitely
while true; do
    sleep 60
done
