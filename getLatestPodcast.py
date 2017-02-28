#!/usr/bin/python2

import xml.dom.minidom
import sys
from contextlib import closing
import urllib2
import pprint

def output(link, title=''):
	if withtitle=="1":
		print title,"\n",link
	else:
		print link
		
withtitle = False
num = 0

if len(sys.argv) > 2:
	num = int(sys.argv[2])
	if len(sys.argv) > 3:
		withtitle = sys.argv[3]

with closing(urllib2.urlopen(sys.argv[1])) as data:
	xml_data = xml.dom.minidom.parse(data)
	item = xml_data.getElementsByTagName('item')[num]
	#link = item.getElementsByTagName('media:content')
	#if (len(link) > 0):
	#	print link[0].getAttribute('url')
	#	exit(0)
	title = item.getElementsByTagName('title')
	link = item.getElementsByTagName('link')
	if (len(link) > 0) and not (item.getElementsByTagName('enclosure')):
		output( link[0].firstChild.data, title[0].firstChild.data )
		exit(0)
	link = item.getElementsByTagName('enclosure')
	if (len(link) > 0):
		output( link[0].getAttribute('url'), title[0].firstChild.data ) 
		exit(0)
	print "NoUrlFound"
	
