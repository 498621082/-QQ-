from nonebot import on_command, CommandSession
from qqbot.botmain import *
from TextToImage.toimage import *
helpmsg = '([]内的为动态填写的内容)\n'\
    '\n\n我现在支持的功能有：\n'\
    '\n使用帮助，指令：[帮助,使用帮助,使用方法]\n'\
    '查看在线服务器，指令：服务器\n'\
    '\n查询世界状态,指令格式:\n'\
    '世界状态 [房间id:数字]\n'\
    '例：世界状态 1\n'\
    '\n查询玩家列表,指令格式:\n'\
    '玩家列表 [房间id:数字]\n'\
    '例：玩家列表 1\n'\
    '\n发送消息到游戏，指令格式:\n'\
    '[房间id:数字] [消息:文字]\n'\
    '例：1 HelloWord\n'\
    '\n发送消息到QQ，指令格式:\n'\
    '@[消息:文字]\n'\
    '例：@HelloWord\n'\
    '\n\n下面指令只能管理员使用\n'\
    '\n1、接收消息(即从游戏里接收消息),指令格式\n'\
    '接收 [开/关]\n'\
    '例：接收 开\n'\
    '\n2、发送消息(即从qq里发送消息)，指令格式\n'\
    '发送 [开/关]\n'\
    '例：发送 开\n'\
    '\n3、艾特发送设置(即游戏里的消息开头加上@才能发送到群里),指令格式:艾特发送 开/关\n'


# '4、管理员发送(即只能管理员发送qq消息到游戏里),指令格式:管理员发送 开/关\n'
@on_command('usage', only_to_me=False, aliases=['使用帮助', '帮助', '使用方法'])
async def _(session: CommandSession):
    ctx = session.ctx.copy()
    if "group_id" in ctx.keys():
        text_to_img(helpmsg, 800)
        ImageMessage = "[CQ:image,file=new_car.jpg]"
        await session.send(ImageMessage)
    return
