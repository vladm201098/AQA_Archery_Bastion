# -*- encoding=utf8 -*-
__author__ = "Vladislav"

"""
INFO
  #coordinate_win = (545, 692)
  #coordinate_lose = (541, 784)

Предпочтительные координаты для первой точки:
x , y Template(r"tpl1664380830669.png", record_pos=(0.409, -0.101)

Предпочтительные координаты для второй точки:
x , y Template(r"tpl1664380843876.png", record_pos=(-0.469, 0.22)
  Template(r"tpl1664380850112.png", record_pos=(-0.471, 0.256)

Координата y = 0.1603, с каждым шагом значение меняется на +0.0065, что позволяет увеличивать дальность стрельбы,
не упуская цель.

"""



from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=ADBORI&&touch_method=MINITOUCH",])


def strike_in_enemy(y):
    #swipe(Template(r"tpl1664379316388.png", record_pos=(0.409, -0.101), resolution=(1080, 1920)), vector=[-0.471, 0.256],duration=1)
    swipe(Template(r"tpl1664377325992.png", record_pos=(0.351, -0.202), resolution=(1080, 1920)), vector=[-0.7000, y],duration=1)
    print(y)
   

def check_and_strike():
    i = 1
    y = 0.11003
    
    while i < 20:
        status_win = exists(Template(r"tpl1664381712816.png", record_pos=(0.005, -0.248), resolution=(1080, 1920)))
        #print(status_win)
        status_lose = exists(Template(r"tpl1664381817494.png", record_pos=(0.001, -0.164), resolution=(1080, 1920)))
        #print(status_lose)
        # Cравниваем с координатами картинок , координаты указаны в инфо
        if status_win == (545, 692):
            i = i + 1000
            #print(i)
            print("win")
            return status_win
        elif status_lose == (541, 784):
            i = i + 1000
            #print(i)
            print('Lose')
            return status_lose

        if i < 20:
            strike_in_enemy(y)
            sleep(10)
            i = i + 1
            y = y + 0.0065
            #print(i)

#check_and_strike()


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)