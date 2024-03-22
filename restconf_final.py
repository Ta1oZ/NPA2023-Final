import json
import requests
requests.packages.urllib3.disable_warnings()

student_id = "64070156"
# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback {}".format(student_id)

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback 64070156",
        "description": "My RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
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


# def delete():
#     resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
#         <!!!REPLACEME with URL!!!>, 
#         auth=basicauth, 
#         headers=<!!!REPLACEME with HTTP Header!!!>, 
#         verify=False
#         )

#     if(resp.status_code >= 200 and resp.status_code <= 299):
#         print("STATUS OK: {}".format(resp.status_code))
#         return "<!!!REPLACEME with proper message!!!>"
#     else:
#         print('Error. Status Code: {}'.format(resp.status_code))


# def enable():
#     yangConfig = <!!!REPLACEME with YANG data!!!>

#     resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
#         <!!!REPLACEME with URL!!!>, 
#         data=json.dumps(<!!!REPLACEME with yangConfig!!!>), 
#         auth=basicauth, 
#         headers=<!!!REPLACEME with HTTP Header!!!>, 
#         verify=False
#         )

#     if(resp.status_code >= 200 and resp.status_code <= 299):
#         print("STATUS OK: {}".format(resp.status_code))
#         return "<!!!REPLACEME with proper message!!!>"
#     else:
#         print('Error. Status Code: {}'.format(resp.status_code))


# def disable():
#     yangConfig = <!!!REPLACEME with YANG data!!!>

#     resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
#         <!!!REPLACEME with URL!!!>, 
#         data=json.dumps(<!!!REPLACEME with yangConfig!!!>), 
#         auth=basicauth, 
#         headers=<!!!REPLACEME with HTTP Header!!!>, 
#         verify=False
#         )

#     if(resp.status_code >= 200 and resp.status_code <= 299):
#         print("STATUS OK: {}".format(resp.status_code))
#         return "<!!!REPLACEME with proper message!!!>"
#     else:
#         print('Error. Status Code: {}'.format(resp.status_code))


# def status():
#     api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

#     resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
#         <!!!REPLACEME with URL!!!>, 
#         auth=basicauth, 
#         headers=<!!!REPLACEME with HTTP Header!!!>, 
#         verify=False
#         )

#     if(resp.status_code >= 200 and resp.status_code <= 299):
#         print("STATUS OK: {}".format(resp.status_code))
#         response_json = resp.json()
#         admin_status = <!!!REPLACEME!!!>
#         oper_status = <!!!REPLACEME!!!>
#         if admin_status == 'up' and oper_status == 'up':
#             return "<!!!REPLACEME with proper message!!!>"
#         elif admin_status == 'down' and oper_status == 'down':
#             return "<!!!REPLACEME with proper message!!!>"
#     elif(resp.status_code == 404):
#         print("STATUS NOT FOUND: {}".format(resp.status_code))
#         return "<!!!REPLACEME with proper message!!!>"
#     else:
#         print('Error. Status Code: {}'.format(resp.status_code))
