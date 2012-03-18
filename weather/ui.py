import getweather as weather
import curses
import curses.panel
# -*- coding: utf-8 -*-

try:
	stdstr = curses.initscr()
	screen = stdstr.subwin(10, 20, 0, 0)
	screen.box()
	
	screen.addstr(1,2, 'first line')
	screen.addstr(2,2, 'second line')


	stdstr.refresh()
	stdstr.getch()

	s = curses.newwin(5,10,2,1)
	s.box()
	s.refresh()
	s.getch()
	


finally:
	curses.endwin()

