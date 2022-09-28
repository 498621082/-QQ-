from nonebot import on_command, CommandSession
from qqbot.botmain import *
from nonebot.log import logger
from common.constant import *
schedulMsg = '{}:{}\n'


@nonebot.scheduler.scheduled_job('cron', second='*')
async def _():
    bot = nonebot.get_bot()
    keylist = red.red.keys(pattern=PLAYCHATKEY.format("*"))
    for key in keylist:
        keystr = bytes.decode(key)
        while 1:
            data = red.red.rpop(keystr)
            if data == None:
                break
            logger.info(data)
            try:
                strdata = bytes.decode(data)
                strdatadict = eval(strdata)
                stage = strdatadict["stage"]
                senddata = None
                if str(stage) == "1":
                    groupId = strdatadict["groupId"]
                    sessionId = strdatadict["sessionId"]
                    roomId = red.red.hget(
                        PLAYCHATKEYLINE.format(groupId, sessionId), "id")
                    aite = red.red.hget(QQCHATKEYINFO.format(groupId), "@")
                    gamePlayRoomId = bytes.decode(roomId)
                    gamePlayName = strdatadict["name"]
                    gamePlayMessage = strdatadict["message"]
                    senddata = "【{}:{}】:{}" .format(
                        gamePlayRoomId, gamePlayName, gamePlayMessage)
            except Exception as e:
                logger.error("发送接收游戏消息错误:{}".format(e))
            if senddata != None and (aite == "0" or senddata.find("@") != -1):
                await bot.send_group_msg(group_id=int(groupId), message=senddata)
