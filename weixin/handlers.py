# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
from .util import wechat, get_wxjs_config


class MessageHandler(RequestHandler):
    def post(self):
        self.write('')
        return

    def get(self):
        """
        处理微信的echostr验证消息
        :return:
        """
        echostr = self.get_argument('echostr')
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            self.write(echostr)
        else:
            print "check signature failed"
            self.write("check signature failed")


class SignHandler(RequestHandler):
    """ 微信js-sdk注册
    """
    def get(self):
        config = get_wxjs_config(self.get_argument('url'), wechat)
        self.write({
            "ret": 0,
            "config": config
        })
