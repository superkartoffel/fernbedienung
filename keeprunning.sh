#!/bin/bash

log_found=`ps -ef|grep -v grep|grep "sudo nodejs /home/pi/webserver/server.js"`
if [ "$log_found" == '' ] ; then
	echo "Starting server"
	nohup sudo nodejs /home/pi/webserver/server.js > /home/pi/webserver/server.log 2>&1 &
else
	echo "Server already running."
fi
