#!/usr/bin/env python
#-*- coding:utf8 -*-



import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	CSRF_ENABLED = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'desk.lee@139.com'
	FLASKY_ADMIN = 'FLASKY_ADMIN'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	#SQLALCHEMY_DATABASE_URI = "mysql://root:whoami!@localhost/test_opsdev"
	MAIL_SERVER = 'smtp.139.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USERNAME = "desk.lee@139.com"
	MAIL_PASSWORD = "139@com123"

config = {
	'development': DevelopmentConfig,
}
