# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def check_popup_noads():
    coordinate = (537, 365)
    currently_status = exists(PopupNoadsLocators.tired_of_ads)
    if currently_status == coordinate:
        print("There is page with No ADS")
    else:
        print("There isn't page with No ADS")
    return currently_status
    

def check_popup_troll():
    coordinate = (538, 431)
    currently_status = exists(PopupTrollLocators.master_troll)
    if currently_status == coordinate:
        print("There is page with Troll")
    else:
        print("There isn't page with Troll")
    return currently_status


def check_popup_merlin():
    currently_status = exists(PopupMerlinLocators.mage_merlin)
    return currently_status    


def exit_popup_noads():
    status_popup = check_popup_noads()
    if status_popup==(537, 365):
        print("Window NO ADS is open")
        touch(PopupNoadsLocators.cross_popup_button)
        
        
def exit_popup_troll():
    status_popup = check_popup_troll()
    if status_popup==(538, 431):
        print("Window Troll is open")
        touch(PopupTrollLocators.cross_popup_button)

        
def exit_popup_merlin():
    status_popup = exists(PopupMerlinLocators.mage_merlin)
    if status_popup == check_popup_merlin():
        touch(PopupMerlinLocators.cross_popup_button)
        
        
#exit_popup_noads()     #Manual start test      
#exit_popup_troll()     #Manual start test
exit_popup_merlin()      #Manual start test

#check_popup_noads()    #Manual start test 
#check_popup_troll()    #Manual start test
#check_popup_merlin()   #Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)