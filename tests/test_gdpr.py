# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
from AQA_Archery_Bastion.core.core_gdpr import *


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:45027/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH", ])



def check_debug_in_build(): # Проверка на наличие дебаггера
    
    sleep(20.0)
    check_value = exists(DebaggerLocators.window_debug) 
    sleep(3.0)
    print(check_value)
    if check_value is False:
        pass
    else:
        key_back()
    

def check_link_terms(): # Проверка линки на достоверность
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Terms of Servise.")


def check_link_privacy(): # Проверка линки на достоверность
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Privacy Policy.")

    
def start_test_gdpr():
    
    start_app("com.bastion.archers")
    check_debug_in_build()
    gdpr_window()
    touch_terms_button()
    check_link_terms()
    key_back()
    key_back()
    gdpr_window()
    touch_privacy_button()
    check_link_privacy()
    key_back()
    key_back()
    touch_accept_button()
    
    
def test_gdpr_settings():
    gdpr_window()
    touch_terms_button()
    check_link_terms()
    gdpr_window()
    touch_privacy_button()
    check_link_privacy()
    touch_accept_button()
    
#start_test_gdpr() # Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)




