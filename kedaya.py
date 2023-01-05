js_config:
- Container:
  - [5]
  Env: wx_wxCollectionActivity_custom
  KeyWord:
  - - M_WX_ADD_CART_URL
  - - jd_wxCollectionActivityUrl
  - - jd_lzaddCart_activityId
  - - jd_lzkj_wxCollectionActivityId
  - - jd_cjhy_wxCollectionActivityId
  Name: 【kedaya】加购有礼
  Script: wx_wxCollectionActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxDrawActivity_custom
  KeyWord:
  - - M_WX_LUCK_DRAW_URL
  - - LUCK_DRAW_URL
  Name: 【kedaya】幸运大转盘
  Script: wx_wxDrawActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxShopGift_custom
  KeyWord:
  - - jd_wxShopGift_activityUrl
  - - jd_lzkj_wxShopGift_ids
  - - jd_cjhy_wxShopGift_ids
  Name: 【kedaya】店铺礼包
  Script: wx_wxShopGift.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxTeam_custom
  KeyWord:
  - - M_WX_TEAM_URL
  - - jd_zdjr_activityId
  - - jd_cjhy_activityId
  Name: 【kedaya】组队瓜分
  Script: wx_wxTeam.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_pool_custom
  KeyWord:
  - - pool
  Name: 【kedaya】组队瓜分京豆
  Script: wx_pool.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxPointDrawActivity_custom
  KeyWord:
  - - wxPointDrawActivity
  Name: 【kedaya】抽奖赚积分
  Script: wx_wxPointDrawActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxShopFollowActivity_custom
  KeyWord:
  - - jd_cjhy_wxShopFollowActivity_activityId
  - - jd_lzkj_wxShopFollowActivity_activityId
  - - jd_wxShopFollowActivity_activityUrl
  - - jd_wxShopFollowActivity_activityId
  - - M_WX_FOLLOW_DRAW_URL
  Name: 【kedaya】关注店铺
  Script: wx_wxShopFollowActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_drawCenter_custom
  KeyWord:
  - - jd_drawCenter_activityId
  Name: 【kedaya】幸运抽奖
  Script: wx_drawCenter.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxGameActivity_custom
  KeyWord:
  - - jd_cjhy_wxGameActivity_activityId
  - - jd_lzkj_wxGameActivity_activityId
  Name: 【kedaya】无线游戏
  Script: wx_wxGameActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxBuildActivity_custom
  KeyWord:
  - - jd_wxBuildActivity_activityId
  - - jd_lzkj_wxBuildActivity_activityId
  Name: 【kedaya】盖楼有礼
  Script: wx_wxBuildActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_sign_custom
  KeyWord:
  - - cjhy_signActivity_ids
  - - jd_lzkj_signActivity2_ids
  Name: 【kedaya】签到有礼
  Script: wx_sign.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_sevenDay_custom
  KeyWord:
  - - jd_cjhy_sevenDay_ids
  - - jd_lzkj_sevenDay_ids
  Name: 【kedaya】七天签到
  Script: wx_sevenDay.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_microDz_custom
  KeyWord:
  - - jd_wdz_activityId
  - - M_WX_WDZ_ID
  Name: 【kedaya】微定制
  Script: wx_microDz.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxMcLevelAndBirthGifts_custom
  KeyWord:
  - - jd_wxMcLevelAndBirthGifts_activityId
  Name: 【kedaya】等级礼包
  Script: wx_wxMcLevelAndBirthGifts.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_daily_custom
  KeyWord:
  - - jd_cjhy_daily_ids
  - - M_WX_DAILY_GIFT_URL
  Name: 【kedaya】每日抢
  Script: wx_daily.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxCollectCard_custom
  KeyWord:
  - - jd_wxCollectCard_activityId
  - - M_WX_COLLECT_CARD_URL
  Name: 【kedaya】集卡有礼
  Script: wx_wxCollectCard.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxFansInterActionActivity_custom
  KeyWord:
  - - jd_wxFansInterActionActivity_activityId
  Name: 【kedaya】粉丝互动
  Script: wx_wxFansInterActionActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxShareActivity_custom
  KeyWord:
  - - jd_wxShareActivity_activityId
  Name: 【kedaya】分享有礼
  Script: wx_wxShareActivity.js
  TimeOut: 0
  Wait: 5
- Container:
  - [5]
  Env: wx_wxSecond_custom
  KeyWord:
  - - jd_wxSecond_activityId
  Name: 【kedaya】拼手速
  Script: wx_wxSecond.js
  TimeOut: 0
  Wait: 5
- Container:
  - [1,2,3,4]
  Env: jd_wxCartKoi_activityId
  KeyWord:
  - - jd_wxCartKoi_activityId
  Name: 【云上】购物车锦鲤
  Script: jd_wxCartKoi.js
  TimeOut: 0
  Wait: 5
- Container:
  - [1,2,3,4]
  Env: WXGAME_ACT_ID
  KeyWord:
  - - WXGAME_ACT_ID
  Name: 【云上】通用游戏任务
  Script: jd_wxgame.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: computer_activityId
  KeyWord:
  - - computer_activityId
  Name: 【云上】电脑配件
  OverdueTime: 600
  Script: jd_computer.js
  TimeOut: 0
  Wait: 5
- Container:
  - [1,2,3,4]
  Env: jd_fxyl_activityId
  KeyWord:
  - - jd_fxyl_activityId
  Name: 【云上】分享有礼
  Script: jd_share.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_cjhy_wxKnowledgeActivity_activityId
  KeyWord:
  - - jd_cjwxKnowledgeActivity_activityId
  - - jd_cjhy_wxKnowledgeActivity_activityId
  - - jd_wxKnowledgeActivity_activityUrl
  Name: 【云上】CJ知识超人
  RegularRules: cjhy@[\d|a-z]{32}@0
  Script: jd_cjhy_wxKnowledgeActivity.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_lzkj_wxKnowledgeActivity_activityId
  KeyWord:
  - - jd_lzkj_wxKnowledgeActivity_activityId
  - - jd_wxKnowledgeActivity_activityId
  - - jd_wxKnowledgeActivity_activityUrl
  Name: 【云上】LJ知识超人
  RegularRules: lzkj@[\d|a-z]{32}@0
  Script: jd_lzkj_wxKnowledgeActivity.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: PKC_TXGZYL
  KeyWord:
  - - PKC_TXGZYL
  Name: 【PKC】关注有礼-特效
  Script: jd_txgzyl.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: PKC_GZYL
  KeyWord:
  - - PKC_GZYL
  Name: 【PKC】关注有礼
  Script: pkc_gzyl.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_mhurlLis
  KeyWord:
  - - jd_mhurlLis
  Name: 【抽奖】盲盒抽京豆
  Script: jd_mhtask.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_nzmhurl
  KeyWord:
  - - jd_nzmhurl
  Name: 【抽奖】女装盲盒抽京豆
  Script: jd_nzmh.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: DPLHTY
  KeyWord:
  - - DPLHTY
  Name: 【开卡】大牌联合
  Script: jd_opencardLH.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: VENDER_ID
  KeyWord:
  - - VENDER_ID
  Name: 【开卡】入会开卡领取礼包
  Script: jd_card_force.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: JD_JOYOPEN
  KeyWord:
  - - JD_JOYOPEN
  Name: 【开卡】JoyJd任务脚本
  Script: jd_opencard_joyopen.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_wdz_openLuckBag_activityId
  KeyWord:
  - - jd_wdz_openLuckBag_activityId
  Name: 【开卡】微定制-开福袋
  Script: jd_wdz_openLuckBag.js
  TimeOut: 0
  Wait: 5
- Container:
  - [1,2,3,4]
  Env: DPQDTK
  KeyWord:
  - - DPQDTK
  Name: 【签到】店铺签到
  Script: jd_dpqd.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Disable: 0
  Env: M_WX_CENTER_DRAW_URL
  KeyWord:
  - - M_WX_CENTER_DRAW_URL
  Name: 【M系】老虎机抽奖
  OverdueTime: 1800
  Script: m_jd_wx_centerDraw.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Disable: 0
  Env: M_FAV_SHOP_ARGV
  KeyWord:
  - - M_FAV_SHOP_ARGV
  Name: 【M系】收藏有礼
  OverdueTime: 1800
  Script: m_jd_fav_shop_gift.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Disable: 0
  Env: M_FOLLOW_SHOP_ARGV
  KeyWord:
  - - M_FOLLOW_SHOP_ARGV
  Name: 【M系】关注有礼
  OverdueTime: 1800
  Script: m_jd_follow_shop.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: M_WX_SHOP_GIFT_URL
  KeyWord:
  - - M_WX_SHOP_GIFT_URL
  Name: 【M系】关注有礼无线
  OverdueTime: 1800
  Script: m_jd_wx_shopGift.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: M_WX_BUILD_DRAW_URL
  KeyWord:
  - - M_WX_BUILD_DRAW_URL
  Name: 【M系】盖楼领奖
  OverdueTime: 1800
  Script: m_jd_wx_buildDraw.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jinggengInviteJoin
  KeyWord:
  - - jinggengInviteJoin
  Name: 【船长】邀请入会有礼
  Script: jd_jinggengInvite.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_inv_authorCode
  KeyWord:
  - - jd_inv_authorCode
  - - yhyauthorCode
  Name: 【船长】邀请赢大礼
  Script: jd_inviteFriendsGift.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_wxShopGiftId
  KeyWord:
  - - jd_wxShopGiftId
  Name: 【船长】特效关注有礼
  Script: jd_wxShopGift.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_joinCommonId
  KeyWord:
  - - jd_joinCommonId
  Name: 【船长】通用开卡
  Script: jd_joinCommon_opencard.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_shopLeagueId
  KeyWord:
  - - jd_shopLeagueId
  Name: 【船长】开卡-shopLeague系列
  Script: jd_shopLeague_opencard.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_shopCollectGiftId
  KeyWord:
  - - jd_shopCollectGiftId
  Name: 【船长】店铺会员礼包
  Script: jd_shopCollectGift.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_wxCompleteInfoId
  KeyWord:
  - - jd_wxCompleteInfoId
  Name: 【船长】完善信息有礼
  Script: jd_wxCompleteInfo.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: M_WX_SECOND_DRAW_URL
  KeyWord:
  - - M_WX_SECOND_DRAW_URL
  Name: 【M系列】读秒拼手速
  Script: m_jd_wx_secondDraw.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_wxBirthGiftsId
  KeyWord:
  - - jd_wxBirthGiftsId
  Name: 【Faker库】生日礼包
  Script: jd_wxBirthGifts.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: JD_Lottery
  KeyWord:
  - - JD_Lottery
  Name: 【Faker库】joy抽奖机通用
  Script: jd_lotterys.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: VENDER_ID
  KeyWord:
  - - VENDER_ID
  Name: 【Faker库】入会开卡领取礼包通用
  Script: jd_card_force.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: whx_drawShopGift
  KeyWord:
  - - whx_drawShopGift
  Name: 【小埋】关注有礼-自动解析通用
  Script: jd_whx_drawShopGift.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: prodevactCode
  KeyWord:
  - - prodevactCode
  Name: 【小埋】邀请好友入会赢好礼
  Script: jd_prodev.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_lzkj_daily_ids
  KeyWord:
  - - jd_lzkj_daily_ids
  Name: 【Faker】lzkj每日抢
  Script: jd_lzkj_daily.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_txzj_lottery_id
  KeyWord:
  - - jd_txzj_lottery_id
  Name: 【Faker】txzj抽奖通用
  Script: jd_txzj_lottery.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_txzj_sign_in_id
  KeyWord:
  - - jd_txzj_sign_in_id
  Name: 【Faker】收藏大师签到
  Script: jd_txzj_sign_in.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_txzj_collect_item_id
  KeyWord:
  - - jd_txzj_collect_item_id
  Name: 【Faker】收藏大师关注有礼
  Script: jd_txzj_collect_item.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_lzkjInteractId
  KeyWord:
  - - jd_lzkjInteractId
  Name: 【船长】Interact邀请有礼
  Script: jd_lzkjInteract.py
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_lzkj_interactsaas_yqrhyl_activityId
  KeyWord:
  - - jd_lzkj_interactsaas_yqrhyl_activityId
  Name: 【Faker】lzkj邀请入会有礼
  Script: jd_lzkj_interact_yqrhyl.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_shop_draw_ids
  KeyWord:
  - - jd_shop_draw_ids
  Name: 【Faker】环境店铺抽奖
  Script: jd_shop_draw.js
  TimeOut: 0
  Wait: 2
- Container:
  - [1,2,3,4]
  Env: jd_shopGifts_ids
  KeyWord:
  - - jd_shopGifts_ids
  Name: 【Faker】环境店铺礼包
  Script: jd_shopGifts.js
  TimeOut: 0
  Wait: 2
- Container:
  - []
  Env: jd_txzj_lottery_id
  KeyWord:
  - - jd_txzj_lottery_id
  - - jd_lottery_activityUrl
  Name: 【Faker】收藏大师幸运抽奖
  RegularRules: '@[\d|a-zA-Z]{24}@0'
  Script: jd_txzj_lottery.js
  TimeOut: 0
  Wait: 2
