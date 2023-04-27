# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *


if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&ori_method=ADBORI&touch_method=ADBTOUCH&",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")


def key_back(): # Назад - выход из дебаггера
    keyevent("BACK")  


def gdpr_window(): # Ожидание загрузки окна GDPR
    wait(GDPRLocators.logo_azurgames)  


def touch_terms_button(): # Ожидание загрузки 
    touch(GDPRLocators.terms_button)
    
    
def touch_privacy_button(): # Ожидание загрузки
    touch(GDPRLocators.privacy_button)
    
    
def touch_accept_button():
    touch(GDPRLocators.accept_gdpr_button)
   

