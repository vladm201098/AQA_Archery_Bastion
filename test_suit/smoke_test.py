# -*- encoding=utf8 -*-
"""
1.Очистка данных - Test 503
2.Запуск билда
3.Загрузочный экран - Test 300
4.GDRP - Test 100-103
5.Rate US -Test 200-202

6.0 1 lvl
6.1 Play - Test 301
6.2 Restart - Test 302 
6.3 Menu - Test 303
6.4 Try again(Restart) - Test 304
6.5 Lose(Menu) - Test 305
6.6 Win - Test 306

7.0 2 lvl + test of boomb - Test 307

8.0 Upgrade - не прописана логика
8.1 Upgrade Army - Test 308
8.2 Upgrade Gear - Test 309
8.3 Upgrade Castle - Test 310

9.0 Setting - Test 311
9.1 Clickable links GDPR - Test 312
9.2 Clickable check-box of settings - Test 313
9.3 Ok/cross ingame window - Test 314

10.0 3 lvl + offer no ads - Test 315
11.4-6 lvl + offer troll - Test 316


12.Основыне локации (по граничным значениям)

13.Troll
14.Store
15. Heroes window's

"""

__author__ = "Vladislav"
__device__ = 'Samsung'

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.tests.test_common import *
from AQA_Archery_Bastion.core.first_level import *
from AQA_Archery_Bastion.core.second_level import *
from AQA_Archery_Bastion.core.third_level import *
from AQA_Archery_Bastion.core.fourth_level import *
from AQA_Archery_Bastion.core.fifth_level import *
from AQA_Archery_Bastion.core.sixth_level import *
from AQA_Archery_Bastion.tests.test_ingame import *
from AQA_Archery_Bastion.core.core_ads import *
from AQA_Archery_Bastion.core.core_settings import *
from AQA_Archery_Bastion.tests.test_settings import *
from AQA_Archery_Bastion.core.popups_offers import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")
    
using("C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion/locators")


#1.1-5 пункт
#test_common()
'''
#6. 1 lvl
play_level_button()
print("Test 301 - PASSED (Play)")
restart_level_resume_test()
print("Test 302 - PASSED (Restart)")
menu_level_ingame()
print("Test 303 - PASSED (Menu)")
play_level_button()
try_again_ingame()
print("Test 304 - PASSED (Try again - Restart)")
lose_menu_ingame()
print("Test 305 - PASSED (Lose - Menu)")

win_ingame()
print("Test 306 - PASSED (Win)")


#7.0 2 lvl Использование бустера(ов)
second_level()
print("Test 307 - PASSED (2 lvl + test of boomb)")
exit_popup_merlin()

#8.0 Upgrade


#9.0 Settings
test_open_settings()
print("Test 311 - PASSED (Settings)")

#9.1 Clicable links GDPR - Test 312
sleep(2)
test_link_gdpr()
sleep(2)
test_gdpr_settings()
print("Test 312 - PASSED (Clicable links GDPR)")

#9.2 Clickable check-boxes of settings - Test 313
sleep(2)
test_open_settings()
sleep(2)
test_check_boxes()
print("Test 313 - PASSED (Clickable check-boxes of settings)")
print("Test 314 - PASSED (Ok/cross ingame window)")


#10.0 3 lvl + offer no ads
third_level()
sleep(5)
check_ads_int()
sleep(5)

exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)
print("Test 315 - PASSED (3 lvl + offer no ads)")
'''

#11.4-6 lvl + offer troll - Test 316
fourth_level()
sleep(5)
check_ads_int()
sleep(5)
exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)

fifth_level()
sleep(5)
check_ads_int()
sleep(5)
exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)

sixth_level()
sleep(5)
check_ads_int()
sleep(5)
exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupTrollLocators.master_troll, PopupMerlinLocators.cross_popup_button)


#12.Основыне локации (по граничным значениям)


#Открывает дебаггер-репортер
open_debug_reporter()
sleep(3)
fill_the_field(15)
sleep(3)
close_debug_reporter()
sleep(5)

#Запуск 15 лвла
fifteenth_level()
sleep(5)
check_ads_int()
sleep(5)
exit_popup(PopupNoadsLocators.tired_of_ads, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupMerlinLocators.mage_merlin, PopupMerlinLocators.cross_popup_button)
exit_popup(PopupTrollLocators.master_troll, PopupMerlinLocators.cross_popup_button)

#Odysseus




from airtest.report.report import simple_report
simple_report(__file__, logpath=None)

