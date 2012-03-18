#!/usr/bin/env python

import web
from web.contrib.template import render_mako

urls = ("/.*", "hello")

app = web.application(urls, globals())


render = render_mako(
		directories = ['templates'],
		input_encoding = 'utf-8',
		output_encoding = 'utf-8',
		)

class hello:
	def GET(self):
		return render.hello(name='Lex')

if __name__ == "__main__":
	app.run()
