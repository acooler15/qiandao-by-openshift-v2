#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-07-30 12:21:48

import os
import hashlib
import urlparse

debug = False
gzip = True
bind = os.getenv('OPENSHIFT_DIY_IP')
port = int(os.getenv('OPENSHIFT_DIY_PORT'))
https = bool(os.getenv('ENABLE_HTTPS', False))
cookie_days = 5
# mysql_url = urlparse.urlparse(os.getenv('OPENSHIFT_MYSQL_DB', ''))
#redis_url = urlparse.urlparse(os.getenv('REDISCLOUD_URL', ''))

class mysql(object):
    host = os.getenv('OPENSHIFT_MYSQL_DB_HOST')
    port = os.getenv('OPENSHIFT_MYSQL_DB_PORT')
    database = os.getenv('OPENSHIFT_APP_NAME', 'qiandao')
    user = os.getenv('OPENSHIFT_MYSQL_DB_USERNAME')
    passwd = os.getenv('OPENSHIFT_MYSQL_DB_PASSWORD')

class sqlite3(object):
    path = './database.db'

# 数据库类型，修改 sqlite3 为 mysql 使用 mysql
db_type = os.getenv('DB_TYPE', 'sqlite3')

# redis 连接参数，可选
class redis(object):
    host = os.getenv('OPENSHIFT_REDIS_HOST') or 'localhost'
    port = os.getenv('OPENSHIFT_REDIS_PORT') or 6379
    passwd = os.getenv('REDIS_PASSWORD') or None
    db = int(os.getenv('REDIS_DB_INDEX', 1))
evil = 100

pbkdf2_iterations = 400
aes_key = hashlib.sha256(os.getenv('AES_KEY', 'binux')).digest()
cookie_secret = hashlib.sha256(os.getenv('COOKIE_SECRET', 'binux')).digest()
check_task_loop = 10000
download_size_limit = 1*1024*1024
proxies = []

# 域名
#domain = 'qiandao.today'
domain = os.getenv('OPENSHIFT_APP_DNS')

# mailgun 邮件发送, 域名和 apikey
# 使用smtp时填写mail_smtp，若使用smtp_ssl则填写mail_smtp_ssl
# mail_smtp填写格式：mail_smtp = "smtp服务器:端口号",mail_smtp_ssl格式相同
mail_smtp = ""
mail_smtp_ssl = ""
mail_user = ""
mail_password = ""
mail_domain = ""
mailgun_key = ""

# google analytics
ga_key = ""

try:
    from local_config import *
except ImportError:
    pass
