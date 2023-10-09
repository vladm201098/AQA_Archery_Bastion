# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.core.data_clean import *
from AQA_Archery_Bastion.tests.test_gdpr import *
from AQA_Archery_Bastion.tests.test_rate_us import *
from AQA_Archery_Bastion.core.loading_screen import *

'''
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",], project_root="C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion")
 '''   
using("C:/Users/Vladislav/Downloads/AirtestIDE/AirtestIDE/AQA_Archery_Bastion/locators")
    
def test_common(): 
    clear_app("com.bastion.archers")
    start_data_clean()
    print("Test 503 - PASSED (Data clean is done)")
    sleep(5.0)
    start_app("com.bastion.archers")
    touch(CommonLocators.icon_archery)
    sleep(15.0)
    check_loading_screen()
    print("Test 300 - PASSED (Loading screen)")
    sleep(15.0)
    start_test_gdpr()
    print("Test 100-103 - PASSED (Testing GDPR is done)")
    sleep(5.0)
    start_test_rateus()
    print("Test 200-202 - PASSED (Testing rate US is done)")
    
    
#test_common()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
