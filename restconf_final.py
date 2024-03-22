import json
import requests
requests.packages.urllib3.disable_warnings()

student_id = "64070156"
# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback{}".format(student_id)

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback64070156",
        "description": "My RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": False,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.30.156.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
} 

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is created successfully".format(student_id)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot create: interface loopback {}".format(student_id)


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is deleted successfully".format(student_id)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback {}".format(student_id)


def enable():
    yangConfig = {
    "ietf-interfaces:interface":{
        "name":"Loopback64070156",
        "description":"My RESTCONF loopback",
        "type":"iana-if-type:softwareLoopback",
        "enabled":True
    }
}

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return"Interface loopback {} is enabled successfully".format(student_id)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return"Cannot enable: Interface loopback {}".format(student_id)


def disable():
    yangConfig = {
    "ietf-interfaces:interface":{
        "name":"Loopback64070156",
        "description":"My RESTCONF loopback",
        "type":"iana-if-type:softwareLoopback",
        "enabled":False
    }
}

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is shutdowned successfully".format(student_id)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot shutdown: Interface loopback {}".format(student_id)


def status():
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback{}".format(student_id)

    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json['ietf-interfaces:interface']['admin-status']
        oper_status = response_json['ietf-interfaces:interface']['oper-status']
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback {} is enabled".format(student_id)
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback {} is disabled".format(student_id)
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback {}".format(student_id)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
