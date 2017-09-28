#coding:utf-8

import sys
import codecs
import re as regex
from bs4 import BeautifulSoup

fo = open("sol.txt", "w+")

for i in range(1, 100, 1):
	fs = open('xxx_' + str(i) + '.html', 'r+',)

	html = fs.read()

	soup=BeautifulSoup(html, "html.parser")
	for line in soup.select('ul.zi li a'):
		zhPattern = regex.compile(u"([\u4e00-\u9fa5])")
		line_s = str(line)
		line_s = line_s.decode("utf-8")
		match = zhPattern.findall(line_s)

		w_Patten = regex.compile(r"^zi(.*)\.html")
		m = w_Patten.findall(line.get('href'))
		
		if match and m:
			fo.write(match[0].encode('utf-8'))
			fo.write('\t')
			fo.write(m[0])
			fo.write('\t')
			fo.write(str(i))
			fo.write('\t')
			fo.write('\r\n')

f.close
