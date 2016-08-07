#!/usr/bin/env python
#-*- coding:utf8 -*-
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from app import my_app


if __name__ == '__main__':
    http_server = WSGIServer(('',8008), my_app, handler_class=WebSocketHandler)
    http_server.serve_forever()
