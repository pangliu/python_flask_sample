# -*- coding: utf-8 -*-
from host_app.data_model.device_model import DeviceInfo
# import command
import subprocess
import threading
import time
import os
import json

# APP_PACKAGE_NAME = 'com.example.uitest.hank.uitestsample'
# APP_TESTCASE_NAME = 'com.example.uitest.hank.uitestsample.RxjavaSampleTest'
# PROJECT_PATH = '/Users/hank/Documents/Android_Example/UItestSample'
# APP_APK_PATH = '/Users/hank/Documents/Android_Example/UItestSample/app/build/outputs/apk/androidTest/debug/'

APP_PACKAGE_NAME = 'com.simulation.alipay.fdi.alipaysimulation'
APP_TESTCASE_NAME = 'com.simulation.alipay.fdi.alipaysimulation.AlipayLoginTest'
APP_APK_PATH = '/Users/hank/Documents/fdi_work/Android/FDI.Payment.Android/app/build/outputs/apk/androidTest/debug'
PROJECT_PATH = '/Users/hank/Documents/fdi_work/Android/FDI.Payment.Android'
APP_APK_NAME = 'app-debug-androidTest.apk'

class GetDeviceInfoTask:

    def __init__(self):
        # 先下 adb devices 抓 devices id
        cmdStatus,respStr = subprocess.getstatusoutput('adb devices')
        respArray = respStr.split('\n')
        # print 'array size', len(respArray)
        deviceArray = []
        for index in range(len(respArray)):
            if index>0 and index<len(respArray)-1:
                devices = respArray[index].split('\t')
                print('dev', devices)
                deviceArray.append(devices[0])
        self.device_serial_array = deviceArray

    # 取得所有手機 serial number
    def get_devices_serial(self):
        return self.device_serial_array

    # 取得所有手機的資訊
    def get_all_devices_info(self):
        self.phone_info_list = []
        threads = []
        i = 0
        for device in self.device_serial_array:
            threads.append(threading.Thread(target = self.get_device_info, args = (device,)))
            threads[i].start()
            # threads[i].join()
            i = i+1
        j = 0
        for device in self.device_serial_array:
            threads[j].join()
            j = j+1

        # info_str = json.dumps(self.phone_info_list)
        # print(info_str)
        # 回傳 dict
        return self.phone_info_list

    # 取得指定手機資訊
    def get_device_info(self, device_id):
        phone_info = DeviceInfo()
        phone_info.phone_serialno = device_id
        # print 'device_serial_no: ' + device_id
        adb_asign = 'adb -s ' + device_id
        # 取得 versionCode
        command_get_version_code = adb_asign + ' shell dumpsys package ' + APP_PACKAGE_NAME + ' | grep versionCode'
        x,y = subprocess.getstatusoutput(command_get_version_code)
        # print y
        code_info_array = y.strip().split(" ")
        i = 0
        for item in code_info_array:
            info = item.split("=")
            if(info[0] == 'versionCode'):
                version_code = info[1]
                break
            i = i+1
        phone_info.app_version_code = version_code
        # 取得 versionName
        command_get_version_name = adb_asign + ' shell dumpsys package ' + APP_PACKAGE_NAME + ' | grep versionName'
        x,y = subprocess.getstatusoutput(command_get_version_name)
        # print y
        name_info_array = y.strip().split(" ")
        for item in name_info_array:
            info = item.split("=")
            if(info[0] == 'versionName'):
                version_name = info[1]
                break
        # print 'version_name: ' + version_name
        phone_info.app_version_name = version_name
        # 取得 os version
        command_get_on_version = adb_asign + ' shell getprop ro.build.version.release'
        x,y = subprocess.getstatusoutput(command_get_on_version)
        os_version = y.strip()
        # print 'os_version: ' + os_version
        phone_info.phone_os_version = os_version
        # 取得 MacAddress
        command_get_wifi_mac_address = adb_asign + ' shell ip addr show wlan0  | grep "'"link/ether "'"| cut -d"'" "'" -f6'
        x,y = subprocess.getstatusoutput(command_get_wifi_mac_address)
        mac_address = y.strip()
        # print 'mac_address: ' + mac_address
        phone_info.phone_wifi_mac = mac_address
        # 取得電量
        command_get_battery = adb_asign + ' shell dumpsys battery'
        x,y = subprocess.getstatusoutput(command_get_battery)
        phone_battery_status = y.strip().split('\n')
        for item in phone_battery_status:
            info = item.split(":")
            if(info[0].strip() == 'level'):
                phone_battery_level = info[1].strip()
                break
        # print 'phone_battery_level: ' + phone_battery_level
        phone_info.phone_battery_level = phone_battery_level
        # 取得 IMEI
        command_get_phone_imei = adb_asign + " shell \"service call iphonesubinfo 1 | toybox cut -d \\\"'\\\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'\""
        x,y = subprocess.getstatusoutput(command_get_phone_imei)
        phone_imei = y.strip()
        phone_info.phone_imei = phone_imei
        # 取得 手機型號
        command_get_phone_type = adb_asign + ' shell getprop ro.product.model'
        x,y = subprocess.getstatusoutput(command_get_phone_type)
        phone_type = y.strip()
        phone_info.phone_type = phone_type
        
        try:
            # 將字串轉為 josn，放入 dict
            data = json.loads(phone_info.get_info_json())
            self.phone_info_list.append(data)
        except AttributeError:
            pass

        return phone_info