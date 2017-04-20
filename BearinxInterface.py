import os
import sys
import re
import importlib
import pandas
from CMS.CrossMapService import CrossMapService

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(DIR_PATH + "/CMS")
sys.path.append(DIR_PATH + "/CMS/command")

"""
Bearinxインターフェース
"""
class BearinxInterface:
	SYS_HEAD = "CrMp>"
	fullPath = ""
	headLine = None
	indexLine = None

	def __init__(self,path = "",headLine = None,indexLine = None):
		self.fullPath = path
		self.headLine = headLine
		self.indexLine = indexLine

	def cmsPathOpen(self,path,headLine = None,indexLine = None):
		return CrossMapService(path,headLine,indexLine)

	def cmsDesc(self,cmsObj):
		print(cmsObj.crossMapOrigin)

	def cmsCommandCall(self,cmsObj,command):
		itr = command.split(" ")
		commandName = itr.pop(0)
		options = []
		for i in itr:
			options.append(i)
		cmsObj.commandCall(commandName,options)
