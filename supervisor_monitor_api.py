#!/usr/bin/python
import xmlrpclib
import json
import sys

server = xmlrpclib.Server('http://localhost:9001/RPC2')
supervisor_all_info = server.supervisor.getAllProcessInfo()

nargs = len(sys.argv)

def supervisor_discovery():
    services = []
    for process in supervisor_all_info:
        services.append({"{#SUPERVISOR_SERVICE}": process["name"] })
    print(json.dumps({'data' : services }))

def supervisor_service_state():
    service_state = service_status["statename"]
    if service_state == "RUNNING":
        print("20")
    elif service_state == "STOPPED":
        print("0")
    elif service_state == "STARTING":
        print("10")
    elif service_state == "BACKOFF":
        print("30")
    elif service_state == "STOPPING":
        print("40")
    elif service_state == "EXITED":
        print("100")
    elif service_state == "FATAL":
        print("200")
    elif service_state == "UNKNOWN":
        print("1000")
    else:
        print("Script does not work")

def supervisor_service_uptime():
    service_uptime = service_status["now"] - service_status["start"]
    print(service_uptime)

if nargs == 1:
    supervisor_discovery()
elif nargs == 3:
    supervisor_service = sys.argv[1]
    supervisor_service_option = sys.argv[2]
    service_status = server.supervisor.getProcessInfo(supervisor_service)
    if supervisor_service_option == "state":
        supervisor_service_state()
    elif supervisor_service_option == "uptime":
        supervisor_service_uptime()
    else:
        print("Wrong Argument")
else:
    print("You have to set second argument")


