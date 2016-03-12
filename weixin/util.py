# -*- coding: utf-8 -*-
from urllib import unquote
from wechat_sdk import WechatBasic
from settings import WEIXIN

def get_wxjs_config(url, wx_tool):
    url = unquote(url)
    param = {
        "debug": False,
        "jsApiList": ['onMenuShareTimeline', 'onMenuShareAppMessage', 'onMenuShareQQ', 'onMenuShareWeibo'],
        "url": url
    }
    config = wx_tool.get_js_config(param)
    return config


# 实例化 wechat
wechat = WechatBasic(
    token=WEIXIN["WEIXIN_TOKEN"],
    appid=WEIXIN["WEIXIN_APP_ID"],
    appsecret=WEIXIN["WEIXIN_APP_SECRET"]
)
