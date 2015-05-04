# clem-web
web interface for clementine and in future for other players which supports dbus and mpris interface.

WARNING: Still under development. It can not run as daemon and it prints debugigng output to error pages so it can be currently security risk.

# Usage
just run script called clem-web.py. Server starts to listen on all v4 addresses on port 8080. If you can connect to your server only from machine where i is running o, you have to allow tcp port 8080 in aour firewall.
Only requirement is python3

#TODO:
* daemonize
* support for more players
* conf file
* commant line args for port, listening addr and debugging/no daemonizing 

####Low priority
* logging file maybe
* optional http auth
