#!/usr/bin/python2

import xml.dom.minidom
import sys
from contextlib import closing
import urllib2
import pprint

def output(link, title=''):
	if withtitle=="1":
		print title.encode('utf-8'),"\n",link
	else:
		print link
		
withtitle = False

if len(sys.argv) > 2:
	withtitle = sys.argv[2]

with closing(urllib2.urlopen(sys.argv[1])) as data:
	xml_data = xml.dom.minidom.parse(data)
	for item in xml_data.getElementsByTagName('item'):
		#link = item.getElementsByTagName('media:content')
		#if (len(link) > 0):
		#	print link[0].getAttribute('url')
		#	exit(0)
		title = item.getElementsByTagName('title')
		link = item.getElementsByTagName('link')
		if (len(link) > 0) and not (item.getElementsByTagName('enclosure')):
			output( link[0].firstChild.data, title[0].firstChild.data )
			continue
		link = item.getElementsByTagName('enclosure')
		if (len(link) > 0):
			output( link[0].getAttribute('url'), title[0].firstChild.data ) 
			continue
		print "NoUrlFound"
	
