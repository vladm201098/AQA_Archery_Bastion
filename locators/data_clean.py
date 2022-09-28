# -*- encoding=utf8 -*-
__author__ = "Vladislav"

import sys
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *


    
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])

def start_data_clean():
    
    wait(CommonLocators.icon_archery) # Поиск иконки на раб столе
    touch(CommonLocators.icon_archery, duration=2) # вызов меню иконки
    touch(CleanDataLocators.about_icon_archery_button) # О приложении
    wait(CleanDataLocators.storage_button) # Поиск хранилища
    touch(CleanDataLocators.storage_button) # Тач хранилище
    touch(CleanDataLocators.clean_storage_button) # Тач очистить хранилище
    touch(CleanDataLocators.ok_button) # ОК
    touch(CleanDataLocators.back_button) # Тач назад
    sleep(2.0)
    touch(CleanDataLocators.back_button) # Тач назад
    print("Data's app is empty")


#start_data_clean() # Manual start test


#generate html report
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)