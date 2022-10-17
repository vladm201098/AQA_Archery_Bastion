# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.core.data_clean import *
from AQA_Archery_Bastion.tests.test_gdpr import *
from AQA_Archery_Bastion.tests.test_rate_us import *
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])



start_data_clean()
print("Data clean is done")
sleep(5.0)
start_test_gdpr()
print("Testing gdpr is done")
sleep(5.0)
start_test_rateus()
print("Testing rate US is done")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)