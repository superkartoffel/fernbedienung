#!/bin/bash

omxplayer_running=`ps -ef|grep -v grep|grep "omxplayer" | grep "mp4\|avi\|mkv"`
if [ "$omxplayer_running" == '' ] ; then
    echo "omxplayer not running. Turning off monitor.";
    /opt/vc/bin/tvservice -p && /opt/vc/bin/tvservice -o
else
	echo "omxplayer running. Turning on monitor."
	monitor_state=`/opt/vc/bin/tvservice -s | grep off`
	if [ "$monitor_state" != '' ] ; then
        /opt/vc/bin/tvservice -p && chvt 1 && chvt 7
    else
        echo "Already turned on. Skipping."
    fi
fi

