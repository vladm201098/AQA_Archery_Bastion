# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

from AQA_Archery_Bastion.core.def_core_first_sixth import *
from AQA_Archery_Bastion.core.first_level import *
from AQA_Archery_Bastion.core.second_level import *
from AQA_Archery_Bastion.core.third_level import *
from AQA_Archery_Bastion.core.fourth_level import *
from AQA_Archery_Bastion.core.fifth_level import *
from AQA_Archery_Bastion.core.sixth_level import *
from AQA_Archery_Bastion.core.popup_noads_and_troll import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")

    
first_level()
sleep(5.0)
second_level()
sleep(5.0)
third_level()
sleep(5.0)
exit_popup_noads()
sleep(5.0)
fourth_level()
exit_popup_noads()
sleep(5.0)
fifth_level()
exit_popup_noads()
sleep(5.0)
sixth_level()
exit_popup_noads()
exit_popup_troll()


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)