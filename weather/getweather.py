#!/usr/bin/env python
# coding = utf-8

import urllib2
import json

def get():
	req = urllib2.Request('http://m.weather.com.cn/data/101010100.html')
	response = urllib2.urlopen(req, timeout=10)
	data_json = response.read()

	return data_json


if __name__ == '__main__':
	data_json = get()
	data = json.loads(data_json)

	print data['weatherinfo']['city'], data['weatherinfo']['date_y'], data['weatherinfo']['week'], data['weatherinfo']['temp1'], data['weatherinfo']['weather1'], data['weatherinfo']['wind1']


