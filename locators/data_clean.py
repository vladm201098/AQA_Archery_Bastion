# -*- encoding=utf8 -*-
__author__ = "Vladislav"

import sys
import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
#from locators import CommonLocators, CleanDataLocators
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class CommonLocators:


    # Common
    icon_archery = Template(r"tpl1662490750512.png", record_pos=(0.079, -0.039), resolution=(1080, 1920)) # Иконка Лучники
    play_level_button = Template(r"tpl1662728980111.png", record_pos=(0.057, 0.236), resolution=(1080, 1920)) # Play Level button
    setting_button = Template(r"tpl1662729047792.png", record_pos=(-0.433, -0.766), resolution=(1080, 1920))
    setting_ingame_button = Template(r"tpl1662732041060.png", record_pos=(-0.435, -0.755), resolution=(1080, 1920))
    ingame_back_button = Template(r"tpl1662732056529.png", record_pos=(-0.005, 0.206), resolution=(1080, 1920))
    ingame_restart_button = Template(r"tpl1662732103721.png", record_pos=(0.003, 0.35), resolution=(1080, 1920))
    upgrade_army_active = Template(r"tpl1662730900577.png", record_pos=(-0.286, 0.458), resolution=(1080, 1920))
    upgrade_army_unactive = Template(r"tpl1662731151771.png", record_pos=(-0.29, 0.459), resolution=(1080, 1920))
    upgrade_gear_active = Template(r"tpl1662731018184.png", record_pos=(-0.05, 0.459), resolution=(1080, 1920))
    upgrade_gear_unactive = Template(r"tpl1662731099217.png", record_pos=(-0.052, 0.462), resolution=(1080, 1920))
    upgrade_castle_active = Template(r"tpl1662731040350.png", record_pos=(0.201, 0.461), resolution=(1080, 1920))
    upgrade_castle_unactive = Template(r"tpl1662731084175.png", record_pos=(0.203, 0.461), resolution=(1080, 1920))
    

class CleanDataLocators:


    # Cleen Data
    about_icon_archery_button = Template(r"tpl1662490950156.png", record_pos=(0.163, -0.238), resolution=(1080, 1920)) # О приложении 
    storage_button = Template(r"tpl1662491095400.png", record_pos=(-0.257, -0.102), resolution=(1080, 1920)) # Хранилище
    clean_storage_button = Template(r"tpl1662491235186.png", record_pos=(-0.176, -0.474), resolution=(1080, 1920)) # Очистить хранилище
    ok_button = Template(r"tpl1662491300727.png", record_pos=(0.296, 0.144), resolution=(1080, 1920)) # OK
    back_button = Template(r"tpl1662491358519.png", record_pos=(-0.449, -0.792), resolution=(1080, 1920)) # Стрелочка назад
    
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


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





#generate html report
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)