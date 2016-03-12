# -*- coding: utf-8 -*-

# webserver config
HOST = "127.0.0.1"
PORT = 9003

DEVELOPMENT = False
# cross domain
XS_DOMAIN = ""


# weixin config
WEIXIN = {
    "WEIXIN_TOKEN": "",
    "WEIXIN_APP_ID": "",
    "WEIXIN_APP_SECRET": "",
    "WEIXIN_ENCODING_AES_KEY": "",
}



## Import local settings
try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()
