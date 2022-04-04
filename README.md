# Auto_Spy_Scripts
Ver：**20220331-010**
**by: https://t.me/windfgg**

分享有礼需要添加变量 `ownCookieNum` 需要助力的CK数量 默认4

**M系统和kedaya教程都相同 kedaya分组并发跑得快不过IP黑的也快 M比稳跑的慢**

## 更新说明

- 开卡入会脚本h5st 接口修改为甘露殿接口
- 添加甘露殿 众筹许愿池、电脑配件任务

## 已知问题
- kedaya_组队 可能跑不了
## 教程

**傻妞容器ID要改**

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
rm -rf /ql/repo/qitoqito_kedaya && ql repo https://github.com/qitoqito/kedaya.git kedaya && cp -a /ql/repo/qitoqito_kedaya/. /ql/scripts && task qitoCreat.js now
```
3. 压缩包里面的js脚本添加进青龙 **切记添加定时任务**
4. 添加机器人`@auto_spy_bot`，点击start
5. 在群里发送`/nolan`，机器人自动发送私钥给你
6. 将脚本和配置文件放到青龙 `scripts/auto_spy/`文件夹下，设置电报和青龙参数，可以建立一个群，用于机器人打印日志
7. 进入青龙容器，运行`cd /ql/scripts/auto_spy` 进入目录 `python3 auto_spy_bot.py`，登录你的tg，登录成功并看到鉴权成功后，ctrl+c退出
8. `python3 auto_spy_bot.py &` 后台持久运行
### 更新说明
进入青龙容器执行
```shell
rm -rf /ql/repo/qitoqito_kedaya && ql repo https://github.com/qitoqito/kedaya.git kedaya && cp -a /ql/repo/qitoqito_kedaya/. /ql/scripts && task qitoCreat.js now
```
即可

