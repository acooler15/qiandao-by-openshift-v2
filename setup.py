#!/usr/bin/env python
from setuptools import setup

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.

setup(name='qiandao', version='1.0',
      description='qiandao with python',
	  install_requires=[
        'tornado',
		'u-msgpack-python',
		'jinja2',
		'chardet',
		'requests'
],
	 dependency_links = [
			'http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df'
		]
     )
