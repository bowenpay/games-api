import tornado.ioloop
import tornado.web
import settings
from raven.contrib.tornado import AsyncSentryClient

application = tornado.web.Application(
    [
        # weixin
        (r"/api/weixin/", "weixin.handlers.MessageHandler"),
        (r"/api/weixin/sign/", "weixin.handlers.SignHandler"),
    ],
    debug=True,
    session_secret = "games-api-cookie-secret"
)

if __name__ == "__main__":
    application.listen(settings.PORT, address=settings.HOST)
    tornado.ioloop.IOLoop.instance().start()
