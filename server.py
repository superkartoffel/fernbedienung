#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

serv = HTTPServer(('',80),CGIHTTPRequestHandler)
serv.serve_forever()
