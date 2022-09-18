# -*- encoding=utf8 -*-
__author__ = "Vladislav"

from airtest.core.api import *
from airtest.cli.parser import cli_setup


class CommonLocators:
    # Common
    icon_archery = Template(r"tpl1662490750512.png", record_pos=(0.079, -0.039),
                            resolution=(1080, 1920))  # Иконка Лучники
    play_level_button = Template(r"tpl1662728980111.png", record_pos=(0.057, 0.236),
                                 resolution=(1080, 1920))  # Play Level button
    setting_button = Template(r"tpl1662729047792.png", record_pos=(-0.433, -0.766), resolution=(1080, 1920))
    setting_ingame_button = Template(r"tpl1662732041060.png", record_pos=(-0.435, -0.755), resolution=(1080, 1920))
    ingame_back_button = Template(r"tpl1662732056529.png", record_pos=(-0.005, 0.206), resolution=(1080, 1920))
    ingame_restart_button = Template(r"tpl1662732103721.png", record_pos=(0.003, 0.35), resolution=(1080, 1920))
    upgrade_army_active = Template(r"tpl1662730900577.png", record_pos=(-0.286, 0.458), resolution=(1080, 1920))
    upgrade_army_unactive = Template(r"tpl1662731151771.png", record_pos=(-0.29, 0.459), resolution=(1080, 1920))
    upgrade_gear_active = Template(r"tpl1662731018184.png", record_pos=(-0.05, 0.459), resolution=(1080, 1920))
    upgrade_gear_unactive = Template(r"tpl1662731099217.png", record_pos=(-0.052, 0.462), resolution=(1080, 1920))
    upgrade_castle_active = Template(r"tpl1662731040350.png", record_pos=(0.201, 0.461), resolution=(1080, 1920))
    upgrade_castle_unactive = Template(r"tpl1662731084175.png", record_pos=(0.203, 0.461), resolution=(1080, 1920))


class DebaggerLocators:
    # MAX Mediation Debagger
    window_debug_default = Template(r"tpl1663250895027.png", record_pos=(-0.256, -0.786), resolution=(1080, 1920))
    window_debug = Template(r"tpl1662711477262.png", record_pos=(-0.421, -0.671),
                            resolution=(1080, 1920))  # APP info, because color can change
    debug_button = Template(r"tpl1662719272821.png", record_pos=(0.405, -0.231), resolution=(1080, 1920))
    showgdpr = Template(r"tpl1662731343803.png", record_pos=(-0.117, -0.753), resolution=(1080, 1920))
    prev_level_button = Template(r"tpl1662731218931.png", record_pos=(-0.118, -0.654), resolution=(1080, 1920))
    debug_lose_button = Template(r"tpl1662731279071.png", record_pos=(-0.119, -0.544), resolution=(1080, 1920))
    debug_win_button = Template(r"tpl1662731310721.png", record_pos=(-0.115, -0.444), resolution=(1080, 1920))
    add_bomb_button = Template(r"tpl1662731495438.png", record_pos=(-0.128, 0.073), resolution=(1080, 1920))
    debug_money_button = Template(r"tpl1662731400113.png", record_pos=(-0.119, 0.179), resolution=(1080, 1920))
    rate_us_button = Template(r"tpl1662731413182.png", record_pos=(-0.115, 0.285), resolution=(1080, 1920))


class GDPRLocators:
    # GDPR
    logo_azurgames = Template(r"tpl1662714601964.png", record_pos=(-0.006, -0.327), resolution=(
    1080, 1920))  # Лого AzurGames Нужно будет потом добавить проверку на нгаличие этого лого
    terms_button = Template(r"tpl1662715762815.png", record_pos=(-0.003, 0.022),
                            resolution=(1080, 1920))  # Terms of Servise button
    privacy_button = Template(r"tpl1662715779089.png", record_pos=(-0.002, 0.094),
                              resolution=(1080, 1920))  # Privacy Policy button
    terms_and_privacy_link = Template(r"tpl1662718230644.png", record_pos=(-0.208, -0.795),
                                      resolution=(1080, 1920))  # Terms of Servise link
    accept_gdpr_button = Template(r"tpl1662715786685.png", record_pos=(-0.003, 0.406),
                                  resolution=(1080, 1920))  # ACCEPT


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/127.0.0.1:62025?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH", ])


    
def start_app():
    touch(CommonLocators.icon_archery)  # Поиск и тач по значку Archery


def debug_windows():
    wait(DebaggerLocators.window_debug)


def check_debug_in_build():
    assert_exists(DebaggerLocators.window_debug, "Check debug windows in build.")  # Проверка на наличие дебаггера


def key_back():
    keyevent("BACK")  # Назад - выход из дебаггера


def Gdpr_window():
    wait(GDPRLocators.logo_azurgames)  # Ожидание загрузки окна GDPR


def touch_terms_button():
    touch(GDPRLocators.terms_button)


def check_link_terms():
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Terms of Servise.")  # Проверка линки на достоверность



def touch_privacy_button():
    touch(GDPRLocators.privacy_button)


def check_link_privacy():
    assert_exists(GDPRLocators.terms_and_privacy_link,
              "Check currectly link in Privacy Policy.")  # Проверка линки на достоверность


def touch_accept_button():
    touch(GDPRLocators.accept_gdpr_button)
    print("OOOOK")

    
start_app()
debug_windows()
check_debug_in_build()
key_back()
Gdpr_window()
touch_terms_button()
check_link_terms()
key_back()
key_back()
Gdpr_window()
touch_privacy_button()
check_link_privacy()
key_back()
key_back()
touch_accept_button()
    


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


