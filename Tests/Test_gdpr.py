# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH", ])



def check_debug_in_build(): # Проверка на наличие дебаггера
    
    sleep(20.0)
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


def gdpr_window(): # Ожидание загрузки окна GDPR
    wait(GDPRLocators.logo_azurgames)  


def touch_terms_button(): # Ожидание загрузки 
    touch(GDPRLocators.terms_button)


def check_link_terms(): # Проверка линки на достоверность
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Terms of Servise.")
    key_back()
    key_back()


def touch_privacy_button(): # Ожидание загрузки
    touch(GDPRLocators.privacy_button)


def check_link_privacy(): # Проверка линки на достоверность
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Privacy Policy.")
    key_back()
    key_back()


def touch_accept_button():
    touch(GDPRLocators.accept_gdpr_button)
    print("PASSED")

    
start_app("com.bastion.archers")
check_debug_in_build()
gdpr_window()
touch_terms_button()
check_link_terms()
gdpr_window()
touch_privacy_button()
check_link_privacy()
touch_accept_button()
    


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



