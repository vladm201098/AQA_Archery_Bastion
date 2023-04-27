# -*- encoding=utf8 -*-
__author__ = "Vladislav"
'''

Тестирование рекламы пока проходит через UI ,позже планируется переход на Unity poco
Тест запускается при нахождении после 3 лвл первой локации

'''


from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *


if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///127.0.0.1:62025",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")



#Interstisial
def check_ads_int():
    sleep(15)
    check_value = exists(CommonLocators.play_level_button)
    if check_value == (602, 1215):
        print("There isn't interstisial ads")
    else:
        print("There is interstisial ads")
        keyevent("Home")
        wait(CommonLocators.icon_archery, timeout = 30)
        touch(CommonLocators.icon_archery)
        wait(CommonLocators.icon_archery, timeout = 30)
    return


    
#Reward - upgrade army/gear/castle , bombs
def check_ads_reward():
    pass


#Banner
def check_ads_banner():
    sleep(5)
    check_value =exists(AdsLocators.place_ads_banner)
    if check_value == (519, 1854):
        print("There isn't banner ads")
    else:
        print("There is banner ads")
    return 
    

#check_ads_int()
#check_ads_banner()
#check_ads_openapp()



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)