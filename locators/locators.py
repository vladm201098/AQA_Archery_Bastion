from airtest.core.api import *


class CommonLocators:


    # Common
    icon_archery = Template(r"tpl1662490750512.png", record_pos=(0.079, -0.039), resolution=(1080, 1920)) # Иконка Лучники
    play_level_button = Template(r"tpl1662728980111.png", record_pos=(0.057, 0.236), resolution=(1080, 1920)) # Play Level button
    setting_button = Template(r"tpl1662729047792.png", record_pos=(-0.433, -0.766), resolution=(1080, 1920))
    ingame_back_button = Template(r"tpl1662732056529.png", record_pos=(-0.005, 0.206), resolution=(1080, 1920))
    ingame_restart_button = Template(r"tpl1662732103721.png", record_pos=(0.003, 0.35), resolution=(1080, 1920))
    upgrade_army_active = Template(r"tpl1662730900577.png", record_pos=(-0.286, 0.458), resolution=(1080, 1920))
    upgrade_army_unactive = Template(r"tpl1662731151771.png", record_pos=(-0.29, 0.459), resolution=(1080, 1920))
    upgrade_gear_active = Template(r"tpl1662731018184.png", record_pos=(-0.05, 0.459), resolution=(1080, 1920))
    upgrade_gear_unactive = Template(r"tpl1662731099217.png", record_pos=(-0.052, 0.462), resolution=(1080, 1920))
    upgrade_castle_active = Template(r"tpl1662731040350.png", record_pos=(0.201, 0.461), resolution=(1080, 1920))
    upgrade_castle_unactive = Template(r"tpl1662731084175.png", record_pos=(0.203, 0.461), resolution=(1080, 1920))
    
    
class CoreGameLocators:
    
    
    setting_ingame_button = Template(r"tpl1662732041060.png", record_pos=(-0.435, -0.755), resolution=(1080, 1920))
    #count_of_enemy =
    victory_logo = Template(r"tpl1663671009641.png", record_pos=(-0.004, -0.248), resolution=(1080, 1920))
    getx2_button = Template(r"tpl1663671052576.png", record_pos=(0.068, 0.407), resolution=(1080, 1920))
    continue_button = Template(r"tpl1663671081825.png", record_pos=(0.001, 0.645), resolution=(1080, 1920))




    
class CleanDataLocators:


    # Cleen Data
    about_icon_archery_button = Template(r"tpl1662490950156.png", record_pos=(0.163, -0.238), resolution=(1080, 1920)) # О приложении 
    storage_button = Template(r"tpl1662491095400.png", record_pos=(-0.257, -0.102), resolution=(1080, 1920)) # Хранилище
    clean_storage_button = Template(r"tpl1662491235186.png", record_pos=(-0.176, -0.474), resolution=(1080, 1920)) # Очистить хранилище
    ok_button = Template(r"tpl1662491300727.png", record_pos=(0.296, 0.144), resolution=(1080, 1920)) # OK
    back_button = Template(r"tpl1662491358519.png", record_pos=(-0.449, -0.792), resolution=(1080, 1920)) # Стрелочка назад
    

class DebaggerLocators:    
    
    
    # MAX Mediation Debagger
    window_debug_default = Template(r"tpl1663250895027.png", record_pos=(-0.256, -0.786), resolution=(1080, 1920))

    window_debug = Template(r"tpl1662711477262.png", record_pos=(-0.421, -0.671), resolution=(1080, 1920)) # APP info, because color can change
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
    logo_azurgames = Template(r"tpl1662714601964.png", record_pos=(-0.006, -0.327), resolution=(1080, 1920)) # Лого AzurGames Нужно будет потом добавить проверку на нгаличие этого лого
    terms_button = Template(r"tpl1662715762815.png", record_pos=(-0.003, 0.022), resolution=(1080, 1920)) # Terms of Servise button
    privacy_button = Template(r"tpl1662715779089.png", record_pos=(-0.002, 0.094), resolution=(1080, 1920)) # Privacy Policy button
    terms_and_privacy_link = Template(r"tpl1662718230644.png", record_pos=(-0.208, -0.795), resolution=(1080, 1920)) # Terms of Servise link
    accept_gdpr_button = Template(r"tpl1662715786685.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)) # ACCEPT


class RateUsLocators:
    
    #Rate US
    
    logo_rate_us = Template(r"tpl1663606776156.png", record_pos=(-0.002, -0.211), resolution=(1080, 1920)) # Надпись Rate us
    submit_button_active  = Template(r"tpl1663607102842.png", record_pos=(0.005, 0.315), resolution=(1080, 1920)) # Кнопка Submit
    submit_button_nonactive = Template(r"tpl1663662505106.png", record_pos=(0.003, 0.306), resolution=(1080, 1920))
    cross = Template(r"tpl1663662652124.png", record_pos=(0.286, -0.278), resolution=(1080, 1920))
    play_markert_logo = Template(r"tpl1663663120655.png", record_pos=(-0.272, -0.788), resolution=(1080, 1920))
    play_markert_back = Template(r"tpl1663663246685.png", record_pos=(-0.449, -0.794), resolution=(1080, 1920))


    rate_us_5 = Template(r"tpl1663662223998.png", record_pos=(0.164, 0.017), resolution=(1080, 1920))
    rate_us_3 = Template(r"tpl1663662574678.png", record_pos=(-0.003, 0.008), resolution=(1080, 1920))
    rate_us_1 = Template(r"tpl1663662599741.png", record_pos=(-0.161, 0.015), resolution=(1080, 1920))







