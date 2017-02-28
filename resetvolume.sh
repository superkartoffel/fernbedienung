#!/bin/bash

if mkdir /var/lock/mylock; then
  echo "Locking succeeded" >>/home/pi/webserver/volout.txt
  out=""
  vol=`cat /home/pi/webserver/volume.txt`
  for i in {1..10} ; do
    out=`sudo /home/pi/webserver/omxplayer/dbuscontrol.sh volume $vol`
    echo "next try..." >>/home/pi/webserver/volout.txt
    if [[ "$out" =~ Volume ]] ; then
      break;
    fi
  done
else
  echo "Lock failed - exit" >&2
  exit 1
fi

rmdir /var/lock/mylock
