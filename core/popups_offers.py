# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def check_popup_noads():
    currently_status = exists(PopupNoadsLocators.tired_of_ads)
    return currently_status
    

def check_popup_troll():
    currently_status = exists(PopupTrollLocators.master_troll)
    return currently_status


def check_popup_merlin():
    currently_status = exists(PopupMerlinLocators.mage_merlin)
    return currently_status    


def exit_popup_noads():
    if check_popup_noads():
        print("Popup NO ADS is open")
        touch(PopupNoadsLocators.cross_popup_button)
        
        
def exit_popup_troll():
    if check_popup_troll():
        print("Popup Troll is open")
        touch(PopupTrollLocators.cross_popup_button)

        
def exit_popup_merlin():
    if check_popup_merlin(): # в if достаточно состояния переменной для определения true/false. Доп условия дописывать не надо
        print("Popup Merlin is open")
        touch(PopupMerlinLocators.cross_popup_button)
        
'''
def exit_popup(*args):
    status_popup = exists(PopupMerlinLocators.args)
    if status_popup: # в if достаточно состояния переменной для определения true/false. Доп условия дописывать не надо
        print("Popup Merlin is open")
        touch(PopupMerlinLocators.cross_popup_button)
        
'''        
#exit_popup_noads()     #Manual start test
#exit_popup_troll()     #Manual start test
#exit_popup_merlin()
#exit_popup(mage_merlin)    #Manual start test

#check_popup_noads()    #Manual start test
#check_popup_troll()    #Manual start test
#check_popup_merlin()   #Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)