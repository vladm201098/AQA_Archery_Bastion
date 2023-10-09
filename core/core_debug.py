# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
from airtest.core.android.touch_methods.base_touch import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])

    

dev = device()



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
   

def open_or_closed_debug(): # Открытие\закрытие окна дебаггера
    multitouch_event = [
    DownEvent((1050, 1170), 0),
    DownEvent((1050, 1280), 1),  # second finger
    SleepEvent(0.5),
    UpEvent(0), UpEvent(1)]
    dev.touch_proxy.perform(multitouch_event)
    #print("The debugger is open/closed")
    sleep(3)

    
    
    
def open_debug_reporter():
    check_value = exists(DebaggerLocators.icon_debug_reporter)
    touch(DebaggerLocators.icon_debug_reporter)
    return check_value


def close_debug_reporter():
    sleep(3.0)
    check_value = exists(DebaggerLocators.close_debug_reporter)
    touch(DebaggerLocators.close_debug_reporter)
    return check_value
    
    
def select_the_field(): # Становимся в место в котором будем вводить команды    
    sleep(3)
    check_value = exists(DebaggerLocators.field_in_debug_reporter)
    touch(DebaggerLocators.field_in_debug_reporter)

def clear_the_field():
    sleep(3)
    check_value_reporter = exists(DebaggerLocators.close_debug_reporter)
    #touch((433, 900)) # Дефолтные параметры консоли в дебаггере
    sleep(3)
    '''
    for i in range(15):
        check_value_field = exists(DebaggerLocators.field_in_debug_reporter)
        if check_value_field is True:
            keyevent("DEL")
            print(check_value_field)
        else:
            return check_value_field
            '''
    #text('test_clear',  = True)
    #text('', enter = True)
    
def fill_the_field(level): # Заполняем поле в консоле
    sleep(3)
    select_the_field()
    text(f'loadlevel {level}', enter=True)
    sleep(3)

    
lvls_to_move = ['15', '30', '45', '60', '75', '90']
    
    
def move_to_level(): #тест запуск перехода по лвлам
    for level in lvls_to_move:
        print(level)
        open_debug_reporter()
        sleep(3)
        fill_the_field(level)
        sleep(3)
        close_debug_reporter()     
        


#Прописать модуль по очистке поля ввода        
        
#clear_the_field()     
#fill_the_field()    
#open_debug_reporter() #Manual start test
#close_debug_reporter() #Manual start test
#check_debug_in_build() #Manual start test
#open_or_closed_debug() #Manual start test
#move_to_level()

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)