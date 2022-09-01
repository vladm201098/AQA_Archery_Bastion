# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *

auto_setup(__file__)


#from poco.drivers.ue4 import UE4Poco
#poco = UE4Poco()


#from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# from poco.drivers.unity3d import UnityPoco
#poco = UnityPoco()
#poco("android.widget.FrameLayout")

for i in range(100):
    if i<100:
        touch(Template(r"tpl1661862774740.png", record_pos=(0.007, 0.23), resolution=(1080, 1920)))
        sleep(3.0)
        touch(Template(r"tpl1662023463559.png", record_pos=(-0.116, -0.445), resolution=(1080, 1920)))
        #touch(Template(r"tpl1661979875856.png", record_pos=(-0.122, 0.184), resolution=(1080, 1920)))
        wait(Template(r"tpl1661873521867.png", record_pos=(0.002, 0.542), resolution=(1080, 1920)))
        sleep(3.0)
        touch(Template(r"tpl1661873615584.png", record_pos=(0.005, 0.542), resolution=(1080, 1920)))
        sleep(5.0)
        print(i)
        if i == 14 or i == 29:
            wait(Template(r"tpl1661875206586.png", record_pos=(0.013, 0.333), resolution=(1080, 1920)))
            touch(Template(r"tpl1661875217019.png", record_pos=(0.031, 0.333), resolution=(1080, 1920)))
