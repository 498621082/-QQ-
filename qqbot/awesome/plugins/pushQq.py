from nonebot import on_command, CommandSession
from qqbot.botmain import *
from nonebot.log import logger
from common.models import *
from qqbot.config import *
from common.constant import *
famineMsgError2 = '发送消息不能为空,详情发送：帮助'
famineMsgError3 = '找不到{}号服务器,请联系群主或管理员'
aliasesList = []
for i in range(1, 10+1):
    if len(aliasesList) < i+1:
        aliasesList.append(str(i))
    else:
        aliasesList[i] = str(i)


@on_command('1', only_to_me=False, aliases=aliasesList)
async def pushqq(session: CommandSession):
    # 去掉消息首尾的空白符
    judgeSenddata = session.current_arg_text
    judgeSenddata = judgeSenddata.replace(" ", "")
    if judgeSenddata == None and judgeSenddata == "":
        await session.send(famineMsgError2)
        return
    roomId = GetlistParameter(session.ctx["raw_message"].split(" "), 0)
    # msgdata = session._current_arg_text.strip()
    msgdata = GetlistParameter(session._current_arg_text.split(" "), 0)
    msgdata1 = GetlistParameter(session._current_arg_text.split(" "), 1)
    ctx = session.ctx.copy()
    savedata = qqChatData()
    sessionId = ""
    if "group_id" in ctx.keys():
        try:
            keylist = red.red.keys(
                pattern=PLAYCHATKEYLINE.format(ctx["group_id"], "*"))
            for key in keylist:
                key_roomId = red.red.hget(key, "id")
                if key_roomId != None and str(bytes.decode(key_roomId)) == roomId:
                    sessionId = str(bytes.decode(
                        red.red.hget(key, "sessionId")))
                    break
            if sessionId == "":
                await session.send(famineMsgError3.format(roomId))
                return
        except Exception as e:
            logger.error(e)

        try:
            savedata.card = ctx["sender"]["card"]
            savedata.nickname = ctx["sender"]["nickname"]
            savedata.message = msgdata
            savedata.card = ctx["sender"]["card"]
            savedata.userId = ctx["sender"]["user_id"]
            savedata.groupId = ctx["group_id"]
            send = red.red.hget(QQCHATKEYINFO.format(savedata.groupId), "send")
            adminSend = red.red.hget(
                QQCHATKEYINFO.format(savedata.groupId), "admin")
            if adminSend != None and str(bytes.decode(adminSend)) == "1" and savedata.userId not in SUPERUSERS:
                await session.send("您不是管理员，没有权限发送")
                return

            if send != None and str(bytes.decode(send)) == "1":
                await session.send("当前发送已关闭")
                return
            else:
                msgfind = FamineInstruction(msgdata, msgdata1)
                if msgfind:
                    if savedata.userId not in SUPERUSERS:
                        await session.send("您不是管理员，没有权限发送控制台指令")
                        return
                    else:
                        savedata.message = msgfind
                red.pushQQ(savedata.groupId, sessionId, str(savedata))
                return
        except Exception as e:
            logger.error(e)
    else:
        pass


# 复活指令校验
def FamineInstruction(GameInstruct, GamePlayer):
    try:
        localresmasg = None
        if GameInstruct == "复活":
            localresmasg = "复活"+" "+GamePlayer
        elif GameInstruct == "复活全部":
            localresmasg = "复活全部"+" "+GamePlayer
        elif GameInstruct == "重生":
            localresmasg = "重生"+" "+GamePlayer
        elif GameInstruct == "重生掉落":
            localresmasg = "重生掉落"+" "+GamePlayer
        elif GameInstruct == "自杀":
            localresmasg = "自杀"+" "+GamePlayer
        elif GameInstruct == "修复":
            localresmasg = "修复"+" "+GamePlayer
        elif GameInstruct == "保存":
            localresmasg = "保存"+" "+GamePlayer
        elif GameInstruct == "重置世界":
            localresmasg = "重置世界"+" "+GamePlayer
        elif GameInstruct == "灭火":
            localresmasg = "灭火"+" "+GamePlayer
        elif GameInstruct == "一无所有":
            localresmasg = "一无所有"+" "+GamePlayer
        return localresmasg
    except Exception as e:
        logger.error(e)
        return localresmasg


# 数组值获取，并校验
def GetlistParameter(ThisList, intex):
    if ThisList != None:
        ThisListlen = len(ThisList)
    else:
        print("数组获取下标参数，数组不能为None")
    if intex >= 0 and intex < ThisListlen:
        return ThisList[intex]
    else:
        print("数组获取下标参数，下标超出范围")
