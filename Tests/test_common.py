# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from 
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


start_data_clean()
print("Data clean is done")

start_test_gdpr()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)