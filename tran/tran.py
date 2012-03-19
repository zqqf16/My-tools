#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
import json

def tran(msg):
	opener = urllib2.build_opener()
	msg = sys.argv[1]
	url_utf = 'http://fanyi.youdao.com/fanyiapi.do?keyfrom=asdfksljl&key=908880018&type=data&doctype=json&version=1.1&q=' + msg 

	result_json = opener.open(url_utf).read()
	return json.loads(result_json)

if __name__ == '__main__':
	green = '\033[0;32m%s\033[0m: \033[0;34m%s\033[0m'
	
	result = tran(sys.argv[1])
	for trans in result['translation']:
		print green % (u'翻译', trans)
	#print u'\033[1;32m翻译\033[0m: \033[1;31m' + tran + '\033[0m'

	try:
		print u'读音: ' + result['basic']['phonetic']
	except:
		pass
	try:
		for explain in result['basic']['explains']:
			print u'解释: ' + explain
	except:
		pass

	try:
		for web in result['web']:
			value_str = ''
			for value in web['value']:
				value_str += value + ', '
	
			print u'网络释义: [' + web['key'] + '] ' + value_str
	except:
		pass
