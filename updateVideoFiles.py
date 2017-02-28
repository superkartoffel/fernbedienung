#!/usr/bin/python2

import os
import urllib

videos = []
for root, dirs, files in os.walk("/media/pi/My Book/FilmeHD/"):
    for file in files:
        if file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".avi"):
             videos.append( "<li><a href=\"?cmd=run&amp;line=sudo pkill omxplayer; omxplayer %22" + urllib.quote(os.path.join(root, file)) + "%22\">" + file + "</a></li>" )

audios = []
#for root, dirs, files in os.walk("/media/pi/My Book/mp3/"):
#    for file in files:
#        if file.endswith(".mp3") or file.endswith(".ogg") or file.endswith(".flac") or file.endswith(".opus"):
#             audios.append( "<li><a href=\"?cmd=run&amp;line=sudo pkill omxplayer; omxplayer " + urllib.quote_plus(os.path.join(root, file)) + "\">" + file + "</a></li>" )

print "Videos #%d Audios #%d"% (len(videos), len(audios))
videos.sort()
audios.sort()

replacements = {'VIDEO-LINKS': "\n".join(videos), 'AUDIO-LINKS': "\n".join(audios)}

with open('/home/pi/webserver/template.html') as infile, open('/home/pi/webserver/remote.html', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)
