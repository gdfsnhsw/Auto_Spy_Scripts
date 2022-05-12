# Auto_Spy_Scripts

Ver：**20220509-013**
**by: https://t.me/FengTools**

分享有礼需要添加变量 `ownCookieNum` 需要助力的CK数量 默认4

**M系统和kedaya教程都相同  推荐使用kedaya**
**kedaya分组并发跑得快不过IP黑的也快 **
**M比稳跑的慢 但是建议M设置`desi JD_COOKIE 1-3` 某些脚本只跑自己的前几个CK**

kedaya token 机器人:[@qitoBot](https://t.me/qitoBot) 发 `token` 获取kedaya token 环境变量 `QITOQITO`

## 更新说明
- 添加pkc关注有礼
- 添加pkc特效关注有礼
## 已知问题
- NULL
## 教程

**傻妞容器ID要改 `[]` 代表所有容器都跑**

![image-20220328192946696](https://pic.rmb.bdstatic.com/bjh/3e4638c0ead038429412991ac716f762.png)

![](https://pic.rmb.bdstatic.com/bjh/24a8ae6d2c6b9f4ccec0b772231b2877.png)

**下面可达鸭脚本的代理 如果socks模式需要安装nodejs依赖 socks-proxy-agent**

1. 在config.sh添加如下环境变量
```shell
## kedaya 基础
export QITOQITO=QgwMwzZTYGADMjF:266283274c977dd71e291fd7cce8a3c4b36df0fbf84b1fce072e7746934165ed:TURINGLAB
export QITOQITO_PLATFORM='qinglong'
export QITOQITO_SYNC=1 #是否定时同步
export QITOQITO_COVER=1 #是否覆盖入口文件

# telegram 通知
export TELEGRAM_TOKEN="xxxxxxx:xxxxxxxxxxxxxxxxxxxxx"
export TELEGRAM_ID='xxxxxxx'
export TELEGRAM_URL="https://xxxxxxx.xxxxxxx.workers.dev"
## 全局JDCOOKIE设置
export JD_COOKIE_MAIN=3 #全局助力主号设置
#export msgWhite='pin1|pin2|pin3'  #全局通知白名单
#export msgBlack='pin1|pin2|pin3'  #全局通知黑名单

## 脚本映射
export QITOQITO_MAP="jd_cjwxTeam,jd_w630=jd_task_wuxian"

export jd_task_wuxian_help=3 #助力的前几个账号
export jd_task_wuxian_expand="openCard=1"
#export jd_task_wuxian_msgWork='jd_ITllJdPufaVu|jd_6fdb5993ac6ee|jd_WbOOhkfzBKQQ' #接受通知的账号 只能使用pin
#export jd_task_wuxian_proxy='socks://xxxxxxx:1688' #无线代理配置

export jd_cjwxTeam_help=3 #助力的前几个账号
export jd_cjwxTeam_expand="openCard=1"
#export jd_cjwxTeam_msgWork='jd_ITllJdPufaVu|jd_6fdb5993ac6ee|jd_WbOOhkfzBKQQ' #接受通知的账号 只能使用pin
#export jd_cjwxTeam_proxy='socks://xxxxxxx:1688' #组队代理配置

export jd_w630_help=3 #助力的前几个账号
export jd_w630_expand="openCard=1"
#export jd_w630_msgWork='jd_ITllJdPufaVu|jd_6fdb5993ac6ee|jd_WbOOhkfzBKQQ' #接受通知的账号 只能使用pin
#export jd_w630_proxy='socks://xxxxxxx:1688' #微定制代理配置
```
2. 修改config.yaml 内所有的**Container字段为你的傻妞容器ID**
2. 使用`config.yaml`替换`auto_spy.yaml`的`js_config`内容
2. 在青龙容器执行下列sh
```shell
# 青龙面板
rm -rf /ql/repo/qitoqito_kedaya && ql repo https://github.com/qitoqito/kedaya.git kedaya && cp -a /ql/repo/qitoqito_kedaya/. /ql/scripts && task qitoCreat.js now
```
3. 压缩包里面的js脚本添加进青龙 **切记添加定时任务**
4. 添加机器人`@auto_spy_bot`，点击start
5. 在群里发送`/nolan`，机器人自动发送私钥给你
6. 将脚本和配置文件放到青龙 `scripts/auto_spy/`文件夹下，设置电报和青龙参数，可以建立一个群，用于机器人打印日志
7. 进入青龙容器，运行`cd /ql/scripts/auto_spy` 进入目录 `python3 auto_spy_bot.py`，登录你的tg，登录成功并看到鉴权成功后，ctrl+c退出
8. `python3 auto_spy_bot.py &` 后台持久运行
### kedaya更新说明
进入青龙容器执行
`rm -rf /ql/repo/qitoqito_kedaya && ql repo https://github.com/qitoqito/kedaya.git kedaya && cp -a /ql/repo/qitoqito_kedaya/. /ql/scripts && task qitoCreat.js now`
即可

## 环境变量对照表

| 环境变量名称            | 说明                |
| ----------------------- | ------------------- |
| M_WX_LUCK_DRAW_URL      | 幸运抽奖            |
| M_WX_ADD_CART_URL       | 加购有礼            |
| M_WX_CENTER_DRAW_URL    | 集卡有礼            |
| M_WX_FOLLOW_DRAW_URL    | 关注店铺抽奖        |
| M_FOLLOW_SHOP_ARGV      | 关注店铺            |
| M_WX_SECOND_DRAW_URL    | 读秒拼手速          |
| M_FAV_SHOP_ARGV         | 收藏有礼            |
| ACTIVITY_ID             | 分享有礼            |
| SHARE_ACTIVITY_ID       | 分享有礼            |
| jd_zdjr_activityId      | zd组队瓜分Id        |
| jd_cjhy_activityId      | cj组队瓜分Id        |
| jd_cjhy_activityUrl     | zd组队瓜分Url       |
| jd_zdjr_activityUrl     | cj组队瓜分Url       |
| jd_wdz_activityId       | 微定制Id            |
| jd_wdz_activityUrl      | 微定制Url           |
| DPQDTK                  | 店铺签到Token &分割 |
| dpactId                 | 通用大牌Id          |
| actId                   | 通用大牌Id          |
| computer_activityId     | 电脑配件            |
| computer_activityIdList | 电脑配件            |
| VENDER_ID               | 入会有礼            |
| jd_mhurlList            | 盲盒抽京豆          |
| jd_redrain_half_url     | 半点京东雨Url       |
| wish_appIdArrList       | 众筹许愿池          |
| wish_appNameArrList     | 众筹许愿池          |
| comm_activityIDList     | jd_joyjd_open      |
| HDID                    |    福袋            |
| PKC_GZYL | PKC关注有礼 |
| PKC_TXGZYL | PKC特效关注有礼 |

