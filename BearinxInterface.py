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
	filePath = ""
	fileName = ""
	fileExtention = ""
	crossMapOrigin = ""
	crossMapAvatar = ""
	headLine = ""
	indexLine = ""

	def __init__(self):
		pass

	def CMSInterface(self,path,headLine = None,indexLine = None):
		cms = CrossMapService(path,headLine,indexLine)
				
	"""CUI操作用"""
	def start(self):
		endFlag = 0
		while endFlag == 0 :
			print( self.SYS_HEAD + "コマンド入力してください（list:関数一覧表示 desc:現在の配列確認 write:書き出し end:終了）" )
			command = input(self.SYS_HEAD)

			if command == "desc":
				print(self.crossMapOrigin)
			elif command == "end":
				endFlag = 1
			elif command == "help":
				self.commandHelp()
			elif command != "":
				itr = command.split(" ")
				commandName = itr.pop(0)
				options = []
				for i in itr:
					options.append(i)				
				self.commandCall( commandName , options )
			else :
				print(command)

if __name__ == "__main__":
	print("ファイルパスを入力してください")
	inputPath = input()
	print("列名付き？ Yes=1 No=0")
	inputHeadLine = input()
	print("行番号付き？ Yes=1 No=0")
	inputIndexLine = input()

	obj = CrossMapFactory(inputPath,inputHeadLine,inputIndexLine)
	obj.start()


