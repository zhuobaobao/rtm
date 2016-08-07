#-*- coding:utf8 -*-
import os,sys

from flask import Flask
from message import MessageServer
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True

app.config.from_object(config["development"])
config["development"].init_app(app)
db.init_app(app)



def my_app(environ, start_response):  
    path = environ["PATH_INFO"]  
    if path == "/":  
        return app(environ, start_response)  
    elif path == "/websocket":
    	dk = Handle_Websocket(environ["wsgi.websocket"],parm_dict["host"])
    	dk.handle_index()
    else:
        return app(environ, start_response)  

import views
