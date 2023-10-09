# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")

using("C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion/locators")

def check_popup(locator):
    return exists(locator)
     
        
def exit_popup(locator,close_locator):
    if check_popup(locator):
        print(f"Popup {locator} is open")
        if assert_exists(close_locator):
            touch(close_locator)
        else:
            print('press claim')
            #touch(PopupHeroesLocators.claim_button_odysseus)

            
exit_popup(PopupHeroesLocators.odysseus, PopupMerlinLocators.cross_popup_button)    #Manual start test
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)    #Manual start test
exit_popup(PopupTrollLocators.master_troll, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupHeroesLocators.frost_ninja, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupNewUnitsLocators.get_new_units, PopupNewUnitsLocators.no_thanks)

#check_popup_noads()    #Manual start test
#check_popup_troll()    #Manual start test
#check_popup_merlin()   #Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)