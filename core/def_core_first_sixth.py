# -*- encoding=utf8 -*-
__author__ = "Vladislav"

"""
INFO
Здесь прописаны функции запуска 1-6 лвл с поп-апами.
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")

    
def play_level_button():
    touch(CommonLocators.play_level_button)
    
    
def success_finish_level():
    touch(CoreGameLocators.continue_button)

    
def choise_button(locators):
    touch(locators)

    
def check_available_button(locators):
    available = exists(locators) 
    if available:
        choise_button(locators)
    

#check_available_button(CoreGameLocators.troll_in_balloon)
#check_available_button(CoreGameLocators.bobm_button)

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
