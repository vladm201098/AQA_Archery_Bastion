# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
#from AQA_Archery_Bastion.core.core_debug import *
from airtest.core.android.touch_methods.base_touch import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])
    
using("C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion/locators")

dev = device()

def open_or_closed_debug(): # Открытие\закрытие окна дебаггера
    multitouch_event = [
    DownEvent((1050, 1125), 0),
    DownEvent((1050, 1200), 1),  # second finger
    SleepEvent(1),
    UpEvent(0), UpEvent(1)]
    dev.touch_proxy.perform(multitouch_event)
    #print("The debugger is open/closed")
    sleep(1)
    

def check_app_usage(): # Проверка запущена ли игра , если да- пропуск , нет - запускаем
    if exists(CommonLocators.play_level_button):
        pass
    else:
        start_app("com.bastion.archers")
    sleep(12.0)
    check_debug_in_build()
    
    
def check_debug_in_build(): # Проверка на наличие дебаггера    
    sleep(10.0) 
    if exists(DebaggerLocators.window_debug):
        key_back()


def key_back(): # Назад - выход из дебаггера
    keyevent("BACK")  
       
    
def open_rate_us_window(): # Открытие окна Rate US
    # Можно добавить проверку на поиск этого Элемента в списке
    result = exists(DebaggerLocators.rate_us_button)
    sleep(3.0)
    touch(Template(r"tpl1696940392259.png", record_pos=(-0.119, 0.693), resolution=(1080, 1920)))
    
    
def rating(number_star): # Rating all stars
    sleep(2.0)
    touch(number_star)

    
def check_main_page(): # Проверка нахождения в гл. меню
    return exists(CommonLocators.play_level_button)

    
def rate_us_test_5():
    sleep(5.0)
    status_with_net = exists(RateUsLocators.play_market_logo)
    status_without_net = exists(RateUsLocators.play_market_without_net)
    if status_with_net:
        exists(RateUsLocators.archery_stor_logo)
        sleep(3.0)
        touch(RateUsLocators.play_market_back)
        sleep(3.0)
        key_back()
    else:
        sleep(3.0)
        key_back()
        sleep(3.0)


    
def rateus_do():
    open_or_closed_debug()
    sleep(4.0)
    open_rate_us_window()
    sleep(3.0)
    open_or_closed_debug()
    sleep(3.0)


    
def start_test_rateus():
    #check_app_usage()
    # 1 star
    rateus_do()
    rating(RateUsLocators.rate_us_1)
    touch(RateUsLocators.submit_button_active)
    check_main_page()
    # 2 stars
    rateus_do()
    rating(RateUsLocators.rate_us_2)
    touch(RateUsLocators.submit_button_active)
    check_main_page()
    # 3 stars
    rateus_do()
    rating(RateUsLocators.rate_us_3)
    touch(RateUsLocators.submit_button_active)
    check_main_page()
    # 4 stars
    rateus_do()
    rating(RateUsLocators.rate_us_4)
    touch(RateUsLocators.submit_button_active)
    check_main_page()
    # 5 stars
    rateus_do()
    rating(RateUsLocators.rate_us_5)
    touch(RateUsLocators.submit_button_active)
    rate_us_test_5()
    check_main_page()

    #stop_app("com.bastion.archers")
    
    
'''  
exists(Template(r"tpl1696940249584.png", record_pos=(0.006, 0.274), resolution=(1080, 1920)))

open_or_closed_debug()
sleep(5)
exists(Template(r"tpl1696940392259.png", record_pos=(-0.119, 0.693), resolution=(1080, 1920)))
touch(Template(r"tpl1696940652556.png", record_pos=(-0.115, 0.696), resolution=(1080, 1920)))
open_or_closed_debug()
rating(RateUsLocators.rate_us_1)
touch(RateUsLocators.submit_button_active)

#open_or_closed_debug()

'''
    
#start_test_rateus() # Manual start test
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)