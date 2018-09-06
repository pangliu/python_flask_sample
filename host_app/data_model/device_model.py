import json

class DeviceInfo:
    # phone_serialno = 'phone_serialno'
    # phone_imei = 'phone_imei'
    # phone_number = 'phone_number'
    # phone_wifi_mac = 'phone_wifi_mac'
    # phone_type = 'phone_type'
    # phone_network_status = 'phone_network_status'
    # phone_battery_level = 'phone_battery_level'
    # phone_port_no = 'phone_port_no'
    # phone_os_version = 'phone_os_version'
    # app_version_code = 'app_version_code'
    # app_version_name = 'app_version_name'

    def __init__(self, phone_serialno='', phone_imei='', phone_number='', phone_wifi_mac='', 
                    phone_type='', phone_network_status='', phone_port_no='', 
                    phone_battery_level='', phone_os_version='', app_version_code='',
                    app_version_name=''):
        self.phone_info_json = {
            'phone_serialno':phone_serialno,
            'iMEI':phone_imei,
            'phoneNumber':phone_number,
            'macAddress':phone_wifi_mac,
            'status':phone_network_status,
            'phoneType':phone_type,
            'osVersion':phone_os_version,
            'solfVersionCode':app_version_code,
            'softVersionName':app_version_name,
            'portNo':phone_port_no
        }
        self.phone_serialno = phone_serialno
        self.phone_imei = phone_imei
        self.phone_number = phone_number
        self.phone_wifi_mac = phone_wifi_mac
        self.phone_type = phone_type
        self.phone_network_status = phone_network_status
        self.phone_port_no = phone_port_no
        self.phone_battery_level = phone_battery_level
        self.phone_os_version = phone_os_version
        self.app_version_code = app_version_code
        self.app_version_name = app_version_name

    def set_serialno(self, phone_serialno=''):
        self.phone_serialno = phone_serialno

    def set_imei(self, phone_imei=''):
        self.phone_imei = phone_imei

    def set_phone_number(self, phone_number=''):
        self.phone_number = phone_number

    def set_wifi_mac(self, phone_wifi_mac=''):
        self.phone_wifi_mac = phone_wifi_mac

    def set_phone_type(self, phone_type=''):
        self.phone_type = phone_type

    def set_network_status(self, phone_network_status=''):
        self.phone_network_status = phone_network_status

    def set_port_no(self, phone_port_no=''):
        self.phone_port_no = phone_port_no

    def set_battery_level(self, phone_battery_level=''):
        self.phone_battery_level = phone_battery_level

    def set_os_version(self, phone_os_version=''):
        self.phone_os_version = phone_os_version

    def set_version_code(self, app_version_code=''):
        self.app_version_code = app_version_code

    def set_version_name(self, app_version_name=''):
        self.app_version_name = app_version_name
        

    def get_info_json(self):
        self.phone_info_json = {
            'serialNo':self.phone_serialno,
            'iMEI':self.phone_imei,
            'phoneNumber':self.phone_number,
            'macAddress':self.phone_wifi_mac,
            'status':self.phone_network_status,
            'phoneType':self.phone_type,
            'osVersion':self.phone_os_version,
            'solfVersionCode':self.app_version_code,
            'softVersionName':self.app_version_name,
            'portNo':self.phone_port_no
        }
        return json.dumps(self.phone_info_json)
