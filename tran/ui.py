#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import tran

try:
	main_window = curses.initscr()
	
	curses.start_color()
	curses.use_default_colors()
	curses.init_pair(1,curses.COLOR_RED,0)
	y, x = main_window.getmaxyx()
	main_window.addstr(0, 0, '>>>', curses.color_pair(1))
	main_window.refresh()
	main_window.getch()
	top_win = curses.newwin(y-1, x-1, 1, 0)
	top_win.box()
	top_win.addstr(1,1, 'haha')
	top_win.refresh()
	top_win.getch()

finally:
	curses.endwin()
