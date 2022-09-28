from Translate.TranslateInit import *


# 获取翻译 简体中文
def GetTranslate_CH(frontstr, TranslateList):
    queenstr = frontstr
    if frontstr in TranslateList:
        queenstr = TranslateList[frontstr]
    else:
        print("没有:[{}]的翻译".format(frontstr))
    return queenstr


# 获取玩家预知翻译
def GetPlayerPrefabName(frontstr):
    return GetTranslate_CH(frontstr, PlayerPrefabNameList)


# 获取季节
def GetSeasonString(frontstr):
    return GetTranslate_CH(frontstr, SeasonStringList)
