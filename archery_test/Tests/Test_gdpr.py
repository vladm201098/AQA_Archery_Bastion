# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62001?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])

touch(Template(r"tpl1662047392389.png", record_pos=(-0.244, -0.035), resolution=(1080, 1920))) # Поиск и тач по значку Archery
wait(Template(r"tpl1662050710906.png", record_pos=(-0.006, 0.41), resolution=(1080, 1920))) # Ожидание загрузки окна GDPR
touch(Template(r"tpl1662050761089.png", record_pos=(-0.002, 0.022), resolution=(1080, 1920)))
sleep(3)
assert_exists(Template(r"tpl1662050886188.png", record_pos=(-0.209, -0.794), resolution=(1080, 1920)), "Please fill in the test point.")
keyevent("BACK") # Назад
wait(Template(r"tpl1662052727724.png", record_pos=(0.009, 0.406), resolution=(1080, 1920)))
touch(Template(r"tpl1662052739155.png", record_pos=(0.006, 0.1), resolution=(1080, 1920)))

sleep(3)
assert_exists(Template(r"tpl1662050886188.png", record_pos=(-0.209, -0.794), resolution=(1080, 1920)), "Please fill in the test point.")
keyevent("BACK") # Назад

wait(Template(r"tpl1662052763533.png", record_pos=(-0.004, 0.408), resolution=(1080, 1920)))
touch(Template(r"tpl1662052774187.png", record_pos=(0.007, 0.41), resolution=(1080, 1920)))

print("Ебанный СЕЕЕЕЕКC")






# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)