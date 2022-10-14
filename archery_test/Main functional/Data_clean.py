# -*- encoding=utf8 -*-
__author__ = "Vladislav"
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from locators.locators import Locators
import locators as Locators
from locators import Locators
from locators.locators import icon_archery, play_level_button
from locators.locators import CommonLocators
import locators
from locators import CommonLocators


    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62001?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


wait(icon_archery) # Поиск иконки на раб столе
touch(Template(r"tpl1662043722973.png", record_pos=(-0.244, -0.032), resolution=(1080, 1920)),duration=2) # вызов меню иконки
touch(Template(r"tpl1662044299822.png", record_pos=(-0.162, -0.237), resolution=(1080, 1920))) # О приложении
wait(Template(r"tpl1662044370701.png", record_pos=(-0.283, -0.105), resolution=(1080, 1920))) # Поиск хранилища
touch(Template(r"tpl1662044377019.png", record_pos=(-0.28, -0.103), resolution=(1080, 1920))) # Тач хранилище
touch(Template(r"tpl1662044631432.png", record_pos=(-0.176, -0.477), resolution=(1080, 1920))) # Тач очистить хранилище
touch(Template(r"tpl1662044654043.png", record_pos=(0.298, 0.144), resolution=(1080, 1920))) # ОК
touch(Template(r"tpl1662044667354.png", record_pos=(-0.444, -0.79), resolution=(1080, 1920))) # Тач назад 
touch(Template(r"tpl1662045035323.png", record_pos=(-0.441, -0.79), resolution=(1080, 1920))) # Тач нгазад


#data_clean = Data_clean()
#Data_clean.data_cleans




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)  