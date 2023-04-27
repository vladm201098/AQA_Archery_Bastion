# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
from airtest.core.android.touch_methods.base_touch import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])
dev = device()


def check_debug_in_build(): # Проверка на наличие дебаггера    
    sleep(10.0)
    check_value = exists(DebaggerLocators.window_debug) 
    sleep(3.0)
    print(check_value)
    if check_value is False:
        print("There isn't debugger")
    else:
        print("There is debugger")
        key_back()
   

def open_or_closed_debug(): # Открытие\закрытие окна дебаггера
    multitouch_event = [
    DownEvent((100, 100), 0),
    DownEvent((200, 200), 1),  # second finger
    SleepEvent(1),
    UpEvent(0), UpEvent(1)]
    dev.touch_proxy.perform(multitouch_event)
    #print("The debugger is open/closed")
    sleep(1)
    
#check_debug_in_build() #Manual start test
#open_or_closed_debug() #Manual start test


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)