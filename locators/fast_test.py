# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


connect_device("android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH")

install(r"C:\Реп\AQA_Archery_Bastion\current build\archers_2.64.apk")
sleep(10)
start_app("com.bastion.archers")
sleep(10.0)
stop_app("com.bastion.archers")
clear_app("com.bastion.archers")
    

    

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)