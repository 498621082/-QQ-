<img src="https://thumbnail0.baidupcs.com/thumbnail/d36fdf690ud86eadcabb236208226e3d?fid=456216903-250528-1063158117697997&time=1664344800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-Sx7DIjfKSWArvj16o%2Fo0nY6BdwE%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=511151407382869865&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video" width="10%"> 

  - 作者：幻梦成沙♥LPB♥
  - 联系方式：QQ群【709033796】私群，别人的群，群主知道我

# 目录
- [目录](#目录)
- [饥荒联机版QQ聊天系统，指令](#饥荒联机版qq聊天系统指令)
  - [依赖](#依赖)
  - [API【虽然我写了好像没写一样,懒癌】](#api虽然我写了好像没写一样懒癌)
    - [python依赖配置](#python依赖配置)
      - [常用指令](#常用指令)
    - [运行QQ消息处理模块](#运行qq消息处理模块)
    - [运行数据库](#运行数据库)

# 饥荒联机版QQ聊天系统，指令

## 依赖
| 名字                                                                                                                                                                                                                                                                                           | 简介           | 功能                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------------------- |
| <img src="https://user-images.githubusercontent.com/25968335/120111974-8abef880-c139-11eb-99cd-fa928348b198.png" width="3%">[go-cqhttp](https://docs.go-cqhttp.org/)                                                                                                                           | 机器人框架     | 用于构建机器人的使用环境                 |
| <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fredis.h3399.cn%2F_images%2Fredis-logo-single.png&refer=http%3A%2F%2Fredis.h3399.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1666939031&t=35d73a63cc494e9301bc9ce3fac0102c" width="3%"> [redis](https://redis.io/) | 数据库         | 用于储存QQ的数据和游戏中的数据           |
| <img src="" width="3%">[pybot-master](https://github.com/498621082/pybot-master)                                                                                                                                                                                                               | 机器人功能模块 | 用于处理QQ消息，获取游戏数据，储存QQ数据 |
| <img src="" width="3%"> [mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2517567893)                                                                                                                                                                                               | 饥荒mod        | 用于处理QQ消息，和发送游戏数据到数据库   |

## API【虽然我写了好像没写一样,懒癌】

### python依赖配置
- pip install nonebot
- pip install apscheduler
- pip install Pillow
- pip install flask
- pip install redis
#### 常用指令
- 下载：pip install xxx
- 删除：pip uninstall -y xxx
### 运行QQ消息处理模块
- 终结点：\trunk\qqchat.py
### 运行数据库
- 终结点：\trunk\runflask.py