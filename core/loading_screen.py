# -*- encoding=utf8 -*-
__author__ = "Vladislav"
''''
Здесь прописана логика проверки загрузочного экрана

'''

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def check_loading_screen():
    wait(CommonLocators.loading_screen)
    currently_status = assert_exists(CommonLocators.loading_screen)
    if currently_status == (545, 1659):
        pass
        #print("Loading Screen - OK")
    else:
        #print("Loading Screen - not OK")
        return check_loading_screen
    
    
#check_loading_screen() # Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)