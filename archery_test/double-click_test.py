# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62001?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])

    
touch(Template(r"tpl1662040834079.png", record_pos=(-0.347, 0.814), resolution=(1080, 1920)),times = 20, duration=1)

touch(Template(r"tpl1662040961433.png", record_pos=(-0.329, 0.77), resolution=(1080, 1920)),times=2)




# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)