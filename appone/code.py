# -*- coding: utf-8 -*-

import re
import os

def Code(txt):

	#print(txt)

	txt = re.sub(' +',' ',txt)
	txt = re.sub('　+','',txt)
	txt = re.sub('	+','',txt)

	
	txt = re.sub('\r\n','\n',txt)
	txt = re.sub("\n+",'\n',txt)
	txt = re.sub('\n+ \n+','\n',txt)


	#print(str(txt))

	if txt[len(txt)-1] == '\n':
		txt = txt[:len(txt)-1]

	#print(txt)

	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	symbol = "%，。？／——-+=、|：；～·【】「」“”\n."
	blank = ' '

	#开头的图表
	insert_graph = '<section data-space="0.15;max-width: 100%;"><section style="display: flex;  justify-content: center; width: 100%"><section style="background-color: #c9bb98;height:80px;width: 15px;margin-top: 15px"></section><section style="display: flex;  justify-content: center; width: 100%;align-items: flex-end;"><section style="border: 1px solid #825b3c;min-height: 100px;background-color: #f3f3eb;padding: 20px;z-index: 2;width: 100%"><p style="text-align: justify;font-size: 14px">这里输入的</p></section><section style="height:75px;width:7px;border-right: 2px solid #c9bb98;bottom: 0"></section></section></section><section style="display:block;float:right;height: 7px;border-right: 2px solid #c9bb98;border-bottom: 2px solid #c9bb98;width: 80px"></section></section><p style="margin: 0em 0em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><br/></p>'

	#第一段代码
	insert_first = '<p style="margin: 0em 1em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><span style="font-size: 14px; font-family: 宋体, SimSun;">'

	#中间段代码
	insert_para = '</span><br/></p><p style="margin: 0em 1em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><span style="font-size: 14px; font-family: 宋体, SimSun;">&nbsp;</span></p><p style="margin: 0em 1em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><span style="font-size: 14px; font-family: 宋体, SimSun;">'
	#insert_para = '</span></p><p style="margin: 0em 1em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><span style="font-size: 14px; font-family: 宋体, SimSun;">&nbsp;</span></p><p style="margin: 0em 1em; color: rgb(62, 62, 62); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 18px; white-space: normal; text-align: justify; line-height: 1.5em; word-break: normal !important;"><span style="font-size: 14px; font-family: 宋体, SimSun;">'
	#结尾
	insert_final = '</span></p>'

	count = 0
	#解决 当前字符是英文和标点时：后面只有在中文的时候才有空格
	for i in range(len(txt)-1):
		if txt[i+count] in alpha:
			if txt[i+count+1] not in alpha+symbol+blank:
				txt = txt[0:i+count+1] + ' ' + txt[i+count+1:]
				count = count+1
	#解决 当前字符是汉字的时候：后面只有在英文的时候才有空格
		else:
			if txt[i+count] not in symbol:
				if txt[i+count+1] in alpha:
					txt = txt[0:i+count+1] + ' ' + txt[i+count+1:]
					count = count+1
                
	#解决 每一段之间添加“空白行 + 一个空格”
	count2=0
	for i in range(len(txt)-1):
		if txt[i+count2] == '\n':
			txt = txt[0:i+count2] + insert_para + txt[i+count2:]
			count2 = count2+729
               
	#在第一段和末尾添加代码保证第一段和最后一段显示的正确性
	txt = insert_graph + insert_first + txt + insert_final

	txt = re.sub('\（ +','（',txt)
	txt = re.sub(' +\）','）',txt)
	txt = re.sub(' +',' ',txt)
	txt = re.sub('\n+','\n',txt)


	return txt