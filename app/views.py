#-*- coding:utf8 -*-
from flask import render_template,request

from app import app

import urllib2
import json
import message

msgsrv = message.MessageServer()





def host_query(project):
	url = "https://testops-api.15166.com:14343/host_query?project=%s"%project
	res = urllib2.urlopen(url)
	result = json.loads(res.read())
	return result




@app.route('/',methods=["GET","POST"])
def mainbash():
    return render_template("mainbash.html")

@app.route('/index/',methods=["GET","POST"])
def index():
	project = request.args.get("project")
	host = request.args.get("host")
	host_list = host_query("dzsj").split(",")
	return render_template('index.html',**locals())



@app.route("/test/",methods=["GET","POST"])
def test():
	project = request.args.get("project")
	host_client = request.args.get("host")
	return render_template('test.html',**locals())

@app.route("/processes/",methods=["GET","POST"])
def processes():
	project = request.args.get("project")
	host = request.args.get("host")
	user = request.args.get("user")
	return render_template("processes.html",**locals())

@app.route("/process/",methods=["GET","POST"])
def process():
	project = request.args.get("project")
	host = request.args.get("host")
	pid = request.args.get("pid")
	section = request.args.get("section")
	return render_template("process/%s.html"%section,**locals())
@app.route("/network/",methods=["GET","POST"])
def network():
	project = request.args.get("project")
	host = request.args.get("host")
	states = request.args.get("states")
	socket_family = request.args.get("socket_family")
	socket_type = request.args.get("socket_type")
	states_all = ['ESTABLISHED', 'SYN_SENT', 'SYN_RECV', 'FIN_WAIT1', 'FIN_WAIT2', 'TIME_WAIT', 'CLOSE', 'CLOSE_WAIT',
			  'LAST_ACK',
			  'LISTEN', 'CLOSING', 'NONE']
	return render_template("network.html",**locals())

@app.route("/view_disks/",methods=["GET","POST"])
def view_disks():
	project = request.args.get("project")
	host = request.args.get("host")
	return render_template("disks.html",**locals())



@app.route("/socket_channel/",methods=["GET","POST"])
def socket_channel():
	host_client = request.args.get("host")
	action = request.args.get("action")
	port = 9003
	if request.environ.get('wsgi.websocket'):
		ws = request.environ["wsgi.websocket"]
		while True:
			check_message = ws.receive()
			if check_message is None:
				break
			msgsrv.observers.append(ws)
			if action == "dashboard":
				msgsrv.dashboard(ws,check_message,host_client,port)
			elif action == "processes":
				user = request.args.get("user")
				msgsrv.processes(ws,check_message,host_client,port,user)
			elif action == "process":
				pid = request.args.get("pid")
				section = request.args.get("section")
				msgsrv.process(ws,check_message,host_client,port,pid,section)
			elif action == "network":
				msgsrv.network(ws,check_message,host_client,port)
			elif action == "disks":
				msgsrv.disks(ws,check_message,host_client,port)

	return "Connect!"
