# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *


if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def open_settings(): # Открыть окно settings
    wait(CommonLocators.setting_button)
    click(CommonLocators.setting_button)
    

def open_link_gdpr(): #Нажать на ссылку GDPR
    click(CommonLocators.privacy_settings_button)


def find_check_box(): #Найти чек-бокс
    wait(CommonLocators.check_box_sound_fill)
    
 
def click_check_box_sound():
    result = exists(CommonLocators.check_box_sound_fill)
    if result == (376, 854):    
        click(CommonLocators.check_box_sound_fill)
    else:
        click(CommonLocators.check_box_sound_empty)
        
    
def click_check_box_music():
    result = exists(CommonLocators.check_box_music_fill)
    if result == (376, 961):    
        click(CommonLocators.check_box_music_fill)
    else:
        click(CommonLocators.check_box_music_empty)
 

def click_check_box_vibration():
    result = exists(CommonLocators.check_box_vibration_fill)
    if result == (378, 1059):    
        click(CommonLocators.check_box_vibration_fill)
    else:
        click(CommonLocators.check_box_vibration_empty)   
   

def click_all_check_boxes():
    click_check_box_sound() # Click check box sound
    sleep(2)
    click_check_box_music() # Click check box music
    sleep(2)
    click_check_box_vibration() # Click check box vibration
    sleep(2)
    
    
def click_ok_button():
    wait(CommonLocators.ok_button_settings)
    click(CommonLocators.ok_button_settings)

    
def click_cross_button():
    wait(CommonLocators.ok_button_settings)
    click(CommonLocators.ok_button_settings)
