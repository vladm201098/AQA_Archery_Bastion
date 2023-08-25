# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
#from AQA_Archery_Bastion.core.core_debug import *
from airtest.core.android.touch_methods.base_touch import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])

dev = device()

def check_app_usage(): # Проверка запущена ли игра , если да- пропуск , нет - запускаем
    check_value = exists(CommonLocators.play_level_button)
    print(check_value)
    if check_value is True:
        print("We are in game")
    else:
        print ("We aren't in game. I'm gonna start it")
        start_app("com.bastion.archers")
    sleep(12.0)
    check_debug_in_build()
    
def check_debug_in_build(): # Проверка на наличие дебаггера    
    sleep(10.0)
    check_value = exists(DebaggerLocators.window_debug) 
    sleep(3.0)
    print(check_value)
    if check_value is False:
        print("There isn't debugger")
    else:
        print("There is debugger")
        key_back()
    

def key_back(): # Назад - выход из дебаггера
    keyevent("BACK")  
        
def open_or_closed_debug(): # Открытие\закрытие окна дебаггера
    multitouch_event = [
    DownEvent((100, 100), 0),
    DownEvent((200, 200), 1),  # second finger
    SleepEvent(1),
    UpEvent(0), UpEvent(1)]
    dev.touch_proxy.perform(multitouch_event)
    #print("The debugger is open/closed")
    sleep(1)
    
def open_rate_us_window(): # Открытие окна Rate US
    # Можно добавить проверку на поиск этого Элемента в списке
    touch(DebaggerLocators.rate_us_button)
    
def rating_one(): # 1 star
    sleep(2.0)
    touch(RateUsLocators.rate_us_1)

def rating_two(): # 2 stars   
    sleep(2.0)
    touch(RateUsLocators.rate_us_2)
    
def rating_tree(): # 3 stars
    sleep(2.0)
    touch(RateUsLocators.rate_us_3)     
    
def rating_four(): # 4 stars
    sleep(2.0)
    touch(RateUsLocators.rate_us_4)    

def rating_five(): # 5 stars
    sleep(2.0)
    touch(RateUsLocators.rate_us_5)
    
def touch_submit():
    sleep(5.0)
    touch(RateUsLocators.submit_button_active)
    sleep(5.0)
    
def check_main_page(): # Проверка нахождения в гл. меню
    assert_exists(CommonLocators.play_level_button," Check main page")
    print("We are in main page")

def rate_us_test_5():
    sleep(5.0)
    status_with_net = exists(RateUsLocators.play_market_logo)
    print(status_with_net)
    status_without_net = exists(RateUsLocators.play_market_without_net)
    print(status_without_net)
    if status_with_net == (246, 109):
        assert_exists(RateUsLocators.archery_stor_logo, "Check Archery Bations Page")
        sleep(3.0)
        touch(RateUsLocators.play_market_back)
        sleep(3.0)
        #print("With net")
        key_back()
    else:
        sleep(3.0)
        key_back()
        sleep(3.0)
        #print("Without net")


    
def rateus_do():
    open_or_closed_debug()
    sleep(2.0)
    open_rate_us_window()
    sleep(3.0)
    open_or_closed_debug()
    sleep(2.0)


    
def start_test_rateus():
    check_app_usage()
    # 1 star
    rateus_do()
    rating_one()
    touch_submit()
    check_main_page()
    # 2 stars
    rateus_do()
    rating_two()
    touch_submit()
    check_main_page()
    # 3 stars
    rateus_do()
    rating_tree()
    touch_submit()
    check_main_page()
    # 4 stars
    rateus_do()
    rating_four()
    touch_submit()
    check_main_page()
    # 5 stars
    rateus_do()
    rating_five()
    touch_submit()
    rate_us_test_5()
    check_main_page()

    #stop_app("com.bastion.archers")
    
#start_test_rateus() # Manual start test
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)