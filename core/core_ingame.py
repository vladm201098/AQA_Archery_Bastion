# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *


if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Реп/AQA_Archery_Bastion")

    
def setting_ingame_button():
    touch(CoreGameLocators.setting_ingame_button)
    
    
def restart_ingame_button():
    touch(CoreGameLocators.restart_ingame_button)
    

def menu_ingame_button():
    touch(CoreGameLocators.menu_ingame_button)    

    
def debug_lose_button():
    touch(DebaggerLocators.debug_lose_button)
    
    
#restart_ingame_button()
#setting_ingame_button()    
#menu_ingame_button()    



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)