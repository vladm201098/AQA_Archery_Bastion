# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.core.core_strike import *
from AQA_Archery_Bastion.core.def_core_first_sixth import *
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def third_level():    
    y = 0.155    
    third_play_level_button()
    sleep(5.0)
    strike_in_enemy(y)
    sleep(12.0)
    strike_in_enemy(y + 0.0065)
    sleep(12.0)
    strike_in_enemy(y + 0.0165)
    sleep(5.0)
    success_finish_level()
    print("Third level success finished")
    
#third_level()  #Manual start test   

    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)