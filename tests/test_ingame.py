# -*- encoding=utf8 -*-

'''
6.0 1 lvl
6.1 Play - Test 301
6.2 Restart - Test 302 
6.3 Menu - Test 303
6.4 Try again(Restart) - Test 304
6.5 Lose(Menu) - Test 305
6.6 Win - Test 306

'''
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.core.core_ingame import *
from AQA_Archery_Bastion.locators.locators import *
from AQA_Archery_Bastion.core.core_debug import *
from AQA_Archery_Bastion.core.first_level import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


    
#Restart -302
def restart_level_ingame():
    setting_ingame_button()
    restart_level_test()
    restart_ingame_button()
    restart_level_resume_test()
    #print("Test 302 - PASSED (Restart)")

        
def restart_level_test():
    sleep(3)
    assert_exists(CoreGameLocators.restart_ingame_icon) #Проверка, что на странице есть иконка restart ( красная )
        
    
def restart_level_resume_test():
    sleep(3)
    assert_not_exists(CommonLocators.play_level_button) #Проверка, что на странице нет кнопки play

    
#Menu - Test 303
def menu_level_ingame():
    setting_ingame_button()
    restart_level_test()
    menu_ingame_button()
    restart_level_menu_test()    
    #print("Test 303 - PASSED (Menu)")

def restart_level_menu_test():
    sleep(3)
    assert_exists(CommonLocators.play_level_button) #Проверка, что на странице есть кнопки play
    

#Try again(Restart) - Test 304    
def try_again_ingame():
    try_again_test() # тест на то что есть кнопка рестарт (круглая)
    sleep(1.5)
    open_or_closed_debug() # /Открытие дебаггера
    sleep(1.5)
    debug_lose_button()
    sleep(1.5)
    open_or_closed_debug() # /Закрытие дебаггера
    sleep(1.5)
    try_again_defeat_test() # тест на то что есть кнопка Defeat
    sleep(1.5)
    restart_ingame_button()
    sleep(1.5)
    try_again_test() # тест на то что нет кнопки play/ есть кнопка рестарта(значит на находимся на лвл)
    #print("Test 304 - PASSED (Try again - Restart)")

    
def try_again_test():
    sleep(3)
    assert_exists(CoreGameLocators.setting_ingame_button) #Проверка, что на странице есть кнопка рестарт (круглая)

    
def try_again_defeat_test():
    sleep(3)
    assert_exists(CommonLocators.ingame_defeat_icon) #Проверка, что на странице есть кнопка Defeat


#Lose(Menu) - Test 305
def lose_menu_ingame():
    try_again_test() # тест на то что есть кнопка рестарт (круглая)
    open_or_closed_debug() # /Открытие дебаггера
    sleep(1.5)
    debug_lose_button()
    sleep(1.5)
    open_or_closed_debug() # /Закрытие дебаггера
    sleep(1.5)
    try_again_defeat_test() # тест на то что есть кнопка Defeat
    sleep(2)
    menu_ingame_button()
    lose_menu_test() # тест на то что есть кнопка play
    #print("Test 305 - PASSED (Lose - Menu)")
    
    
def lose_menu_test():
    sleep(3)
    assert_exists(CommonLocators.play_level_button) #Проверка, что на странице есть кнопки play

    
#Win - Test 306
def win_ingame():
    first_level()
    #print("Test 306 - PASSED (Win)")

#restart_level_ingame() #Manual start 
#restart_level_test()
#menu_level_ingame()




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)