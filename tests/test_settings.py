# -*- encoding=utf8 -*-
__author__ = "Vladislav"

'''
1. Проверить наличие на гл экране кнопки settings
2. Открыть окно settings
3. Проверить в открывшимся окне наличие ссылки GDPR
ответ теста 311 

4. Нажать на ссылку GDPR
5. Запустить тест GDPR
6. Завершить тест GDPR
ответ теста 312

7. 1,2 и 3 пункт заново
8. Найти чек-бокс
9. Нажатие на чек-бокс sound effect
10. Нажатие на чек-бокс music
11. Нажатие на чек-бокс vibration
12. Закрытие окна Settings через OK

13. 1,2 и 3 пункт заново
14. 9-11 пункты
ответ теста 313
15. Закрытие окна Settings через крестик
ответ теста 314

'''

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *
from AQA_Archery_Bastion.core.core_settings import *

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")

    
def check_settings_main_page(): #Проверяем наличие на гл меню кнопки settings  
    check_settings_main_page = assert_exists(CommonLocators.setting_button, "Check button of settings on the main page")
    
    
def check_gdpr_link(): #Проверяем наличие на странице настроек есть ссылка GDPR  
    check_gdpr_link = assert_exists(CommonLocators.privacy_settings_button, "Check GDPR link on the settings page")

    
def test_open_settings():
    check_settings_main_page()
    open_settings()
    check_gdpr_link()
    
#test_open_settings() #Manual start

def test_link_gdpr():
    open_link_gdpr()  #Нажать на ссылку GDPR
    # Часть этого модуля реализовано в test_gdpr.py
    
def test_check_boxes():
    find_check_box() # Найти чек бокс
    click_all_check_boxes() # Нажатие на все чек боксы с интервалом
    click_ok_button() # Click Ok and close settings
    
    test_open_settings() # Открываем и проверяем заново работу settings
    click_all_check_boxes() # Нажатие на все чек боксы с интервалом
    click_cross_button() # Click cross and close settings
    
    