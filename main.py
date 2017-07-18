#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author: zhouhongjie@apowo.com
# Date: 2017-07-16 15:12:36

import helper
import argparse

if __name__ == '__main__':
	# parser = argparse.ArgumentParser()
	# parser.add_argument("--url", help = "the url of web")
	# options = parser.parse_args()

	# http://www.soku.com/search_video/q_王者荣耀_orderby_1_limitdate_0?site=14&page=2
	for page in range(1, 99):
		pq = helper.get('http://www.soku.com/search_video/q_王者荣耀_orderby_1_limitdate_0?site=14&page=%d' % page)
		for a in pq('.v-link > a'):
			helper.runCmd('you-get -o ./videos --format=mp4 %s' % a.get('href'))