# -*- coding: utf-8 -*-
import platform
import json
import socket

class HostInfo:
    
    def __init__(self, code='', msg='', mobileNum='', pcName='', hostVersion='', osVersion='', localIP='', data=''):
        self.code = code
        self.msg = msg
        self.mobileNum = mobileNum
        self.pcName = pcName
        self.hostVersion = hostVersion
        self.osVersion = platform.platform()
        self.localIP = socket.gethostbyname(socket.gethostname())
        self.data = data

    def set_code(self, code):
        self.code = code

    def set_msg(self, msg):
        self.msg = msg

    def set_mobileNum(self, mobileNum):
        self.mobileNum = mobileNum

    def set_pcName(self, pcName):
        self.pcName = pcName

    def set_hostVersion(self, hostVersion):
        self.hostVersion = hostVersion

    def set_osVersion(self, osVersion):
        self.osVersion = osVersion

    def set_localIP(self, localIP):
        self.localIP = localIP

    def set_data(self, data):
        self.data = data

    def get_osVersion(self):
        self.osVersion = platform.platform()

    def get_host_info_json(self):
        host_json = {'code': self.code,
                'msg': self.msg,
                'mobileNum': self.mobileNum,
                'pcName': self.pcName,
                'hostVersion': self.hostVersion,
                'osVersion': self.osVersion,
                'localIP': self.localIP,
                'data': self.data}
        return json.dumps(host_json, indent=2,ensure_ascii=False)