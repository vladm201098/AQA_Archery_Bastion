# -*- encoding=utf8 -*-
__author__ = "Vladislav"

"""
INFO

Здесь прописаны основне функции аппгрейда армии, амуниции, замка

"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from AQA_Archery_Bastion.locators.locators import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

upgrade_army_active = Template(r"tpl1664983217004.png", record_pos=(-0.283, 0.458), resolution=(1080, 1920))
upgrade_gear_active = Template(r"tpl1664983250269.png", record_pos=(-0.049, 0.459), resolution=(1080, 1920))
upgrade_castle_active = Template(r"tpl1664983269950.png", record_pos=(0.201, 0.459), resolution=(1080, 1920))


    
def upgrade_army():
    status_value = exists(upgrade_army_active)
    if status_value is True:
        touch(upgrade_army_active)
        print("Upgrade was done")
    else:
        print("Upgrade not avalable(army)")


def upgrade_gear():
    status_value = exists(upgrade_gear_active)
    if status_value is True:
        touch(upgrade_gear_active)
        print("Upgrade was done")
    else:
        print("Upgrade not avalable(gear)")
        
        
def upgrade_castle():
    status_value = exists(upgrade_castle_active)
    if status_value is True:
        touch(upgrade_castle_active)
        print("Upgrade was done")
    else:
        print("Upgrade not avalable(castle)")
        
        
#upgrade_army()    # Manual start test 
#upgrade_gear()    # Manual start test
#upgrade_castle()   # Manual start test

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)