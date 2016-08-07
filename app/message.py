#-*- coding:utf8 -*-
import json
import time
from gevent import sleep,socket
from gevent import monkey
# monkey.patch_socket()


class MessageServer(object):
    def __init__(self):
        self.observers = []

    def dashboard(self,ws,check_message,HOST,PORT):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST,PORT))
            if ws in self.observers:
                while True:
                    s.send(check_message)
                    data_all = ""
                    while True:
                        data = s.recv(1024)
                        data_all = data_all + data
                        if data == "\n\r":break
                    result = eval(json.loads(data_all))
                    load_avg = ' '.join(map(lambda x:str(x),result["get_sysinfo"]["load_avg"]))
                    used_excl = result["get_memory"]["total"] - result["get_memory"]["available"]
                    hostname = result["get_sysinfo"]["hostname"]
                    ws.send(json.dumps({"output":json.dumps(result),"load_avg":load_avg,"used_excl":used_excl,"hostname":hostname,"connect_status":"连接成功"}))
                    sleep(1)
                self.observers.pop(self.observers.index(ws))
        except Exception,e:
            ws.send(json.dumps({"connect_status":"%s"%e}))
            self.observers.pop(self.observers.index(ws))
        s.close()
    def processes(self,ws,check_message,HOST,PORT,user):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST,PORT))
            if ws in self.observers:
                while True:
                    s.send(check_message)
                    data_all = ""
                    while True:
                        if data_all.endswith('\n\r'):
                            break
                        data = s.recv(1024)
                        data_all = data_all +  data
                    result = eval(json.loads(data_all))
                    process_list = result["get_process_list"]
                    user_process_list = [p for p in process_list if p["user"] != "root"]
                    processes_count = len(process_list)
                    user_processes_count = len(user_process_list)
                    if user != "all":
                        process_list = user_process_list
                    process_list = sorted(process_list,key=lambda x:x.get("cpu_percent"),reverse=True)
                    result["get_process_list"] = process_list
                    ws.send(json.dumps({"output":json.dumps(result),"connect_status":"连接成功","processes_count":processes_count,"user_processes_count":user_processes_count}))
                    sleep(1)
                self.observers.pop(self.observers.index(ws))
        except Exception,e:
            ws.send(json.dumps({"connect_status":"%s"%e}))
            self.observers.pop(self.observers.index(ws))
        s.close()
    def process(self,ws,check_message,HOST,PORT,pid,section):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST,PORT))
            if ws in self.observers:
                while True:
                    s.send(check_message)
                    data_all = ""
                    while True:
                        if data_all.endswith('\n\r'):
                            break
                        data = s.recv(1024)
                        data_all = data_all +  data
                    result = eval(json.loads(data_all))

                    ws.send(json.dumps({"output":json.dumps(result),"connect_status":"连接成功"}))
                    sleep(1)
                self.observers.pop(self.observers.index(ws))
        except Exception,e:
            print e
            ws.send(json.dumps({"connect_status":"%s"%e}))
            self.observers.pop(self.observers.index(ws))
        s.close()
    def network(self,ws,check_message,HOST,PORT):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST,PORT))
            if ws in self.observers:
                while True:
                    s.send(check_message)
                    data_all = ""
                    while True:
                        if data_all.endswith('\n\r'):
                            break
                        data = s.recv(1024)
                        data_all = data_all +  data
                    result = eval(json.loads(data_all))
                    ws.send(json.dumps({"output":json.dumps(result),"connect_status":"连接成功"}))
                    sleep(1)
                self.observers.pop(self.observers.index(ws))
        except Exception,e:
            ws.send(json.dumps({"connect_status":"%s"%e}))
            self.observers.pop(self.observers.index(ws))
        s.close()
    def disks(self,ws,check_message,HOST,PORT):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST,PORT))
            if ws in self.observers:
                while True:
                    s.send(check_message)
                    data_all = ""
                    while True:
                        if data_all.endswith('\n\r'):
                            break
                        data = s.recv(1024)
                        data_all = data_all +  data
                    result = eval(json.loads(data_all))
                    ws.send(json.dumps({"output":json.dumps(result),"connect_status":"连接成功"}))
                    sleep(1)
                self.observers.pop(self.observers.index(ws))
        except Exception,e:
            ws.send(json.dumps({"connect_status":"%s"%e}))
            self.observers.pop(self.observers.index(ws))
        s.close()
            



