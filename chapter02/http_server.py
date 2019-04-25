#!/usr/bin/python
#-*- coding: utf-8 -*-

from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 8000

    handler = SimpleHTTPRequestHandler
    server = HTTPServer((ip, port), handler)

    server.serve_forever()
