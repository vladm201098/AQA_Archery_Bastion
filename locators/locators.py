from airtest.core.api import *


class CommonLocators:


    # Common
    icon_archery = Template(r"tpl1662490750512.png", record_pos=(0.079, -0.039), resolution=(1080, 1920)) # Иконка Лучники
    #play_level_button = Template(r"tpl1662728980111.png", record_pos=(0.057, 0.236), resolution=(1080, 1920)) # Play Level button
    play_level_button = Template(r"tpl1692969510764.png", record_pos=(0.072, 0.281), resolution=(1080, 1920)) #Play level button New UI

    setting_button = Template(r"tpl1662729047792.png", record_pos=(-0.433, -0.766), resolution=(1080, 1920))
    check_box_sound_fill = Template(r"tpl1682696698977.png", record_pos=(-0.152, -0.098), resolution=(1080, 1920))
    check_box_music_fill = Template(r"tpl1682696715499.png", record_pos=(-0.152, 0.001), resolution=(1080, 1920))
    check_box_vibration_fill = Template(r"tpl1682696723656.png", record_pos=(-0.151, 0.093), resolution=(1080, 1920))
    check_box_sound_empty = Template(r"tpl1682699127157.png", record_pos=(-0.152, -0.098), resolution=(1080, 1920))
    check_box_music_empty = Template(r"tpl1682699137538.png", record_pos=(-0.152, 0.001), resolution=(1080, 1920))
    check_box_vibration_empty = Template(r"tpl1682699147541.png", record_pos=(-0.151, 0.098), resolution=(1080, 1920))


    privacy_settings_button = Template(r"tpl1682675451728.png", record_pos=(-0.017, -0.195), resolution=(1080, 1920))
    ok_button_settings = Template(r"tpl1682675432460.png", record_pos=(0.013, 0.245), resolution=(1080, 1920))
    ingame_back_button = Template(r"tpl1662732056529.png", record_pos=(-0.005, 0.206), resolution=(1080, 1920))
    ingame_restart_button = Template(r"tpl1662732103721.png", record_pos=(0.003, 0.35), resolution=(1080, 1920))
    ingame_defeat_icon = Template(r"tpl1682675192208.png", record_pos=(-0.003, -0.164), resolution=(1080, 1920))

    upgrade_army_active = Template(r"tpl1662730900577.png", record_pos=(-0.286, 0.458), resolution=(1080, 1920))
    upgrade_army_disactive = Template(r"tpl1662731151771.png", record_pos=(-0.29, 0.459), resolution=(1080, 1920))
    
    upgrade_gear_active = Template(r"tpl1662731018184.png", record_pos=(-0.05, 0.459), resolution=(1080, 1920))
    upgrade_gear_disactive = Template(r"tpl1662731099217.png", record_pos=(-0.052, 0.462), resolution=(1080, 1920))
    
    upgrade_castle_active = Template(r"tpl1662731040350.png", record_pos=(0.201, 0.461), resolution=(1080, 1920))
    upgrade_castle_disactive = Template(r"tpl1662731084175.png", record_pos=(0.203, 0.461), resolution=(1080, 1920))
    loading_screen = Template(r"tpl1670454389916.png", record_pos=(0.005, 0.646), resolution=(1080, 1920))
    attack_button = Template(r"tpl1694192114701.png", record_pos=(-0.004, 0.488), resolution=(1080, 1920))


    
class CoreGameLocators:
    
    
    setting_ingame_button = Template(r"tpl1662732041060.png", record_pos=(-0.435, -0.755), resolution=(1080, 1920))
    #count_of_enemy =
    victory_logo = Template(r"tpl1663671009641.png", record_pos=(-0.004, -0.248), resolution=(1080, 1920))
    getx2_button = Template(r"tpl1663671052576.png", record_pos=(0.068, 0.407), resolution=(1080, 1920))
    continue_button = Template(r"tpl1663671081825.png", record_pos=(0.001, 0.645), resolution=(1080, 1920))
    bobm_button = Template(r"tpl1664377528029.png", record_pos=(-0.298, 0.568), resolution=(1080, 1920))
    restart_ingame_button = Template(r"tpl1664377567555.png", record_pos=(0.003, 0.347), resolution=(1080, 1920))
    restart_ingame_icon = Template(r"tpl1664377852385.png", record_pos=(-0.006, -0.247), resolution=(1080, 1920))
    menu_ingame_button = Template(r"tpl1664377886739.png", record_pos=(-0.007, 0.202), resolution=(1080, 1920))
    cross_ingame_button = Template(r"tpl1664378109082.png", record_pos=(-0.438, -0.754), resolution=(1080, 1920))
    
    troll_in_balloon = Template(r"tpl1692999999424.png", record_pos=(-0.055, -0.4), resolution=(1080, 1920))








    
class CleanDataLocators:


    # Cleen Data
    
    about_icon_archery_button = Template(r"tpl1682623433802.png", record_pos=(-0.164, -0.239), resolution=(1080, 1920))
    storage_button = Template(r"tpl1684957962711.png", record_pos=(-0.313, 0.255), resolution=(1080, 1920))

    clean_storage_button = Template(r"tpl1684957762590.png", record_pos=(-0.24, -0.153), resolution=(1080, 1920))

    about_icon_archery_button_ru = Template(r"tpl1662490950156.png", record_pos=(0.163, -0.238), resolution=(1080, 1920)) # О приложении 
    storage_button_ru = Template(r"tpl1662491095400.png", record_pos=(-0.257, -0.102), resolution=(1080, 1920)) # Хранилище
    clean_storage_button_ru = Template(r"tpl1662491235186.png", record_pos=(-0.176, -0.474), resolution=(1080, 1920)) # Очистить хранилище
    ok_button = Template(r"tpl1684958052279.png", record_pos=(0.298, 0.13), resolution=(1080, 1920)) # OK
    back_button = Template(r"tpl1684958071846.png", record_pos=(-0.448, -0.794), resolution=(1080, 1920))
 # Стрелочка назад
    

class DebaggerLocators:    
    
    
    # MAX Mediation Debagger
    window_debug_default = Template(r"tpl1663250895027.png", record_pos=(-0.256, -0.786), resolution=(1080, 1920))

    window_debug = Template(r"tpl1662711477262.png", record_pos=(-0.421, -0.671), resolution=(1080, 1920)) # APP info, because color can change
    debug_button = Template(r"tpl1662719272821.png", record_pos=(0.405, -0.231), resolution=(1080, 1920))
    showgdpr = Template(r"tpl1662731343803.png", record_pos=(-0.117, -0.753), resolution=(1080, 1920))
    prev_level_button = Template(r"tpl1662731218931.png", record_pos=(-0.118, -0.654), resolution=(1080, 1920))
    debug_lose_button = Template(r"tpl1685013097959.png", record_pos=(-0.113, -0.549), resolution=(1080, 1920))
    debug_lose_button_old = Template(r"tpl1662731279071.png", record_pos=(-0.119, -0.544), resolution=(1080, 1920))
    debug_win_button = Template(r"tpl1662731310721.png", record_pos=(-0.115, -0.444), resolution=(1080, 1920))
    add_bomb_button = Template(r"tpl1662731495438.png", record_pos=(-0.128, 0.073), resolution=(1080, 1920))
    debug_money_button = Template(r"tpl1662731400113.png", record_pos=(-0.119, 0.179), resolution=(1080, 1920))
    #rate_us_button = Template(r"tpl1685050916219.png", record_pos=(-0.113, 0.594), resolution=(1080, 1920))
    rate_us_button = Template(r"tpl1696882753694.png", record_pos=(-0.116, 0.697), resolution=(1080, 1920))


    
    icon_debug_reporter = Template(r"tpl1684411155924.png", record_pos=(0.35, -0.691), resolution=(1080, 1920))
    close_debug_reporter = Template(r"tpl1684415066274.png", record_pos=(0.409, -0.837), resolution=(1080, 1920))
    field_in_debug_reporter = Template(r"tpl1684427950829.png", record_pos=(-0.098, -0.055), resolution=(1080, 1920))

    
class GDPRLocators:    
    
    # GDPR
    logo_azurgames = Template(r"tpl1662714601964.png", record_pos=(-0.006, -0.327), resolution=(1080, 1920)) # Лого AzurGames Нужно будет потом добавить проверку на нгаличие этого лого
    terms_button = Template(r"tpl1691150430372.png", record_pos=(0.0, -0.067), resolution=(1080, 1920)) # Terms of Servise button
    privacy_button = Template(r"tpl1691150450267.png", record_pos=(0.003, 0.067), resolution=(1080, 1920)) # Privacy Policy button
    terms_and_privacy_link = Template(r"tpl1662718230644.png", record_pos=(-0.208, -0.795), resolution=(1080, 1920)) # Terms of Servise link
    accept_gdpr_button = Template(r"tpl1691150800505.png", record_pos=(0.001, 0.42), resolution=(1080, 1920)) # ACCEPT


class RateUsLocators:
    
    #Rate US
    
    logo_rate_us = Template(r"tpl1663606776156.png", record_pos=(-0.002, -0.211), resolution=(1080, 1920)) # Надпись Rate us
    #submit_button_active  = Template(r"tpl1685051014983.png", record_pos=(-0.007, 0.305), resolution=(1080, 1920))
    submit_button_active = Template(r"tpl1696943435824.png", record_pos=(-0.002, 0.306), resolution=(1080, 1920))
                                            # Кнопка Submit
    submit_button_nonactive = Template(r"tpl1663662505106.png", record_pos=(0.003, 0.306), resolution=(1080, 1920))
    cross = Template(r"tpl1682675501550.png", record_pos=(0.285, -0.278), resolution=(1080, 1920))

    play_market_logo = Template(r"tpl1663663120655.png", record_pos=(-0.272, -0.788), resolution=(1080, 1920))
    play_market_without_net = Template(r"tpl1666089609164.png", record_pos=(-0.005, -0.556), resolution=(1080, 1920))

    archery_stor_logo = Template(r"tpl1682621964876.png", record_pos=(-0.094, -0.687), resolution=(540, 960))
    play_market_back = Template(r"tpl1663663246685.png", record_pos=(-0.449, -0.794), resolution=(1080, 1920))
    rate_us_5 = Template(r"tpl1664284721163.png", record_pos=(0.16, 0.019), resolution=(1080, 1920))
    rate_us_4 = Template(r"tpl1664284685358.png", record_pos=(0.08, 0.02), resolution=(1080, 1920))
    rate_us_3 = Template(r"tpl1664284666300.png", record_pos=(-0.001, 0.019), resolution=(1080, 1920))
    rate_us_2 = Template(r"tpl1685047119651.png", record_pos=(-0.081, 0.018), resolution=(1080, 1920))
    rate_us_1 = Template(r"tpl1664282577580.png", record_pos=(-0.162, 0.016), resolution=(1080, 1920))
    

class StartLevelLocators:
    first_play_level_button = Template(r"tpl1664553179625.png", record_pos=(0.059, 0.264), resolution=(1080, 1920))
    second_play_level_button = Template(r"tpl1664553230875.png", record_pos=(0.065, 0.256), resolution=(1080, 1920))
    third_play_level_button = Template(r"tpl1664556321293.png", record_pos=(0.061, 0.262), resolution=(1080, 1920))
    fourth_play_level_button = Template(r"tpl1664556438567.png", record_pos=(0.06, 0.257), resolution=(1080, 1920))
    fifth_play_level_button = Template(r"tpl1664556519478.png", record_pos=(0.059, 0.263), resolution=(1080, 1920))
    sixth_play_level_button = Template(r"tpl1664556636120.png", record_pos=(0.061, 0.258), resolution=(1080, 1920))


class PopupNoadsLocators:
    tired_of_ads = Template(r"tpl1665507240292.png", record_pos=(-0.004, -0.552), resolution=(1080, 1920))
    no_ads_button = Template(r"tpl1665507537362.png", record_pos=(-0.164, 0.422), resolution=(1080, 1920))
    no_ads_extra_button = Template(r"tpl1665507640307.png", record_pos=(0.205, 0.421), resolution=(1080, 1920))
    cross_popup_button = Template(r"tpl1665507692457.png", record_pos=(-0.432, -0.767), resolution=(1080, 1920))


class PopupTrollLocators:
    master_troll = Template(r"tpl1665507968094.png", record_pos=(-0.002, -0.49), resolution=(1080, 1920))
    pay_button = Template(r"tpl1665508015991.png", record_pos=(0.0, 0.431), resolution=(1080, 1920))
    cross_popup_button = Template(r"tpl1665507692457.png", record_pos=(-0.432, -0.767), resolution=(1080, 1920))

    
class PopupMerlinLocators:
    mage_merlin = Template(r"tpl1693324992812.png", record_pos=(-0.005, -0.493), resolution=(1080, 1920))
    watch_ad_button = Template(r"tpl1693325221861.png", record_pos=(0.001, 0.429), resolution=(1080, 1920))

    cross_popup_button = Template(r"tpl1665507692457.png", record_pos=(-0.432, -0.767), resolution=(1080, 1920))

class PopupHeroesLocators:
    odysseus = Template(r"tpl1694794777279.png", record_pos=(-0.005, -0.487), resolution=(1080, 1920))
    pay_button_odysseus = Template(r"tpl1694794815037.png", record_pos=(-0.002, 0.426), resolution=(1080, 1920))
    storm_god = Template(r"tpl1693934739000.png", record_pos=(0.0, -0.485), resolution=(1080, 1920))
    pay_button_storm = Template(r"tpl1693934787291.png", record_pos=(-0.002, 0.423), resolution=(1080, 1920))
    frost_ninja = Template(r"tpl1693935051312.png", record_pos=(0.001, -0.484), resolution=(1080, 1920))
    pay_button_frost = Template(r"tpl1693935080129.png", record_pos=(-0.001, 0.428), resolution=(1080, 1920))

    cross_popup_button = Template(r"tpl1665507692457.png", record_pos=(-0.432, -0.767), resolution=(1080, 1920))

class PopupNewUnitsLocators:
    get_new_units = Template(r"tpl1696859319120.png", record_pos=(0.001, -0.555), resolution=(1080, 1920))
    no_thanks = Template(r"tpl1696859347870.png", record_pos=(0.002, 0.406), resolution=(1080, 1920))
    claim = Template(r"tpl1696859365220.png", record_pos=(0.001, 0.251), resolution=(1080, 1920))


class AdsLocators:
    #interstisial
    
    #reward
    
    #banner
    place_ads_banner = Template(r"tpl1682675639270.png", record_pos=(0.002, 0.84), resolution=(1080, 1920))
    


    #openapp
    

class NewUILocators:
    shop_button = Template(r"tpl1692969810376.png", record_pos=(-0.419, 0.813), resolution=(1080, 1920))


    heroes_button = Template(r"tpl1692972555712.png", record_pos=(-0.101, 0.806), resolution=(1080, 1920))


    
    battle_button = Template(r"tpl1692972942363.png", record_pos=(0.079, 0.801), resolution=(1080, 1920))



    
    gods_button = Template(r"tpl1692972966210.png", record_pos=(0.238, 0.809), resolution=(1080, 1920))


    
    skin_button = Template(r"tpl1692972999497.png", record_pos=(0.415, 0.816), resolution=(1080, 1920))

    


class ShopLocators:
    sell_store = Template(r"tpl1692996060006.png", record_pos=(-0.001, -0.798), resolution=(1080, 1920))
    no_ads_button_in_shop = Template(r"tpl1692996596582.png", record_pos=(-0.019, -0.595), resolution=(1080, 1920))
    #buy_merlin_button_in_shop = 
    #buy_storm_button_in_shop = 
    #buy_kartos_button_in_shop = 
    #buy_frost_button_in_shop =
    #buy_troll_button_in_shop = 
    
    daily_offers = Template(r"tpl1692996099861.png", record_pos=(0.002, -0.627), resolution=(1080, 1920)) # Airtest находит картинку , даже если она находятся за пределами выбранной зоны - т.е. находит если она  есть на экране
    get_coins_free = Template(r"tpl1692997356522.png", record_pos=(-0.316, -0.086), resolution=(1080, 1920))
    get_tokens_free = Template(r"tpl1692997389395.png", record_pos=(-0.005, -0.072), resolution=(1080, 1920))
    get_bombs_free = Template(r"tpl1692997422858.png", record_pos=(0.312, -0.081), resolution=(1080, 1920))
    
    hero_tokens = Template(r"tpl1692996323860.png", record_pos=(0.004, -0.262), resolution=(1080, 1920))
    buy_100_tokens = Template(r"tpl1692997465159.png", record_pos=(-0.338, 0.401), resolution=(1080, 1920))
    buy_1000_tokens = Template(r"tpl1692997489249.png", record_pos=(-0.119, 0.397), resolution=(1080, 1920))
    buy_5000_tokens = Template(r"tpl1692997512134.png", record_pos=(0.112, 0.401), resolution=(1080, 1920))
    buy_20000_tokens = Template(r"tpl1692997536180.png", record_pos=(0.342, 0.402), resolution=(1080, 1920))

    golds = Template(r"tpl1692996334061.png", record_pos=(0.0, 0.217), resolution=(1080, 1920))
    buy_2000_coins = Template(r"tpl1692997616220.png", record_pos=(-0.346, 0.408), resolution=(1080, 1920))
    buy_10000_coins = Template(r"tpl1692997638719.png", record_pos=(-0.12, 0.413), resolution=(1080, 1920))
    buy_50000_coins = Template(r"tpl1692997662152.png", record_pos=(0.115, 0.414), resolution=(1080, 1920))
    buy_120000_coins = Template(r"tpl1692997687628.png", record_pos=(0.344, 0.42), resolution=(1080, 1920))


class TawernLocators:
    pass


class GodsLocators:
    pass


class SkinLocators:
    castle_units = Template(r"tpl1692997754815.png", record_pos=(-0.001, -0.54), resolution=(1080, 1920))
    select_button = Template(r"tpl1692997785942.png", record_pos=(0.005, 0.538), resolution=(1080, 1920))


