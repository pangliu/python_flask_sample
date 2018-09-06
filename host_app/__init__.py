# -*- coding: utf-8 -*-
from flask import Flask, request
from host_app.task.get_device_info_task import GetDeviceInfoTask
from host_app.task.get_bank_detail_task import GetBankDetailTask
from host_app.data_model.device_model import DeviceInfo
from host_app.data_model.host_model import HostInfo
from host_app.config import DevConfig
from host_app.helper.rsa_helper import RsaHelper
import json

app = Flask(__name__)
app.config.from_object(DevConfig)
# app.run(0.0.0.0:5000)

if __name__ == '__main__':
    print('main function')
    # app.debug = True
    app.run('0.0.0.0:5000')

@app.route("/")
def hello():
    return "hello world ssss"

@app.route("/hostInfo", methods=['GET'])
def host_info():
    signMsg = request.headers.get('signMsg')
    # print(signMsg)
    isVerify = RsaHelper.is_sign_msg_verify(signMsg)
    # print(isVerify)
    host_info = HostInfo()
    if(isVerify):
        task_obj = GetDeviceInfoTask()
        device_id = task_obj.get_devices_serial()
        host_info.set_mobileNum(len(device_id))
        if(len(device_id) != 0):
            info_list = task_obj.get_all_devices_info()
            host_info.set_data(info_list)
        host_info.set_code('000')
        host_info.set_msg('請求成功')
        return host_info.get_host_info_json()
    else:
        host_info.set_code('400')
        host_info.set_msg('權限不足')
        return host_info.get_host_info_json()

@app.route("/deviceInfo", methods=['GET'])
def device_info():
    device_id = request.args.get('serialNo')
    print(device_id)
    host_info = HostInfo()
    task_obj = GetDeviceInfoTask()
    serial_list = task_obj.get_devices_serial()
    if(0 == len(serial_list)):
        # 目前沒有與任何手機連線
        return '{}'
    for serial in serial_list:
        if(serial==device_id):
            info = task_obj.get_device_info(device_id)
            # str_info = info.get_info_json()
            # host_info.set_data(str_info)
            # str_resp = host_info.get_host_info_json()
            return str_resp
    # info = task_obj.get_device_info(device_id)
    # str_info = info.get_info_json()
    # return str_info
    # serialNo 不存在
    return '{}'

    