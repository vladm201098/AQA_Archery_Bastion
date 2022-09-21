# -*- encoding=utf8 -*-
__author__ = "Vladislav"


from airtest.core.api import *
from airtest.core.android.touch_methods.base_touch import *


connect_device("Android:///")
# get current device
dev = device()


# 1. tap with two fingers
multitouch_event = [
    DownEvent((100, 100), 0),
    DownEvent((200, 200), 1),  # second finger
    SleepEvent(1),
    UpEvent(0), UpEvent(1)]

dev.touch_proxy.perform(multitouch_event)
sleep(1)

