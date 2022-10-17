# -*- encoding=utf8 -*-
__author__ = "Vladislav"
"""
INFO - Работа без рекламы или с иннапом no ads
Лвл начинается с 3(позже с 7)
"""
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.core.core import *
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])


def identify_continue_restart():
    check_result = check_and_strike()
    if check_result == (545, 692):
        print("prev lvl won")
        touch_continue_button()
        sleep(5.0)
        touch_play_level_button()
    if check_result == (541, 784):
        print("prev lvl lost")
        touch_restart_button()
        
def touch_continue_button():
    touch(CoreGameLocators.continue_button)
    
def touch_restart_button():
    touch(CoreGameLocators.menu_ingame_button)
    sleep(2.0)
    touch(CommonLocators.upgrade_castle_active)
    sleep(2.0)
    touch(CommonLocators.upgrade_gear_active)
    sleep(2.0)
    touch(CommonLocators.upgrade_army_active)
    sleep(2.0)
    touch(CommonLocators.upgrade_army_active)
    sleep(2.0)
    touch_play_level_button()
    #wait(CoreGameLocators.restart_ingame_button)
    #touch(CoreGameLocators.restart_ingame_button)
    # Если игрок лузает , то он выходит и делает аппгрейд, до тех пока пока не выиграет
    
    
    
def touch_play_level_button():
    wait(CommonLocators.play_level_button)
    touch(CommonLocators.play_level_button)
    sleep(7.0) # Ожидание загрузки лвл
    identify_continue_restart()

#touch_play_level_button()
identify_continue_restart()




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)