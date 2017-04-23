import os
import sys
import re
import importlib
import glob
import pandas

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(DIR_PATH + "/command")

"""
二次元表操作用クラス
"""
class CrossMapService:
	SYS_HEAD = "CrMp>"
	fullPath = ""
	filePath = ""
	fileName = ""
	fileExtention = ""
	crossMapOrigin = ""
	crossMapAvatar = ""
	headLine = ""
	indexLine = ""

	"""ファイルパスの指定"""
	def __init__(self,path,headLine = None,indexLine = None):
		if headLine == "0" or headLine == "" or headLine is None :
			self.headLine = None
		else :
			self.headLine = 0

		if indexLine == "0" or headLine == "" or indexLine is None :
			self.indexLine = None
		else :
			self.indexLine = 0	

		self.fullPath = path
		self.pathClassify(path)
		self.crossMapping(path)

	"""パスの分類"""
	def pathClassify(self,path):
		lead = re.search("^.",path)

		if lead == "." or lead == "/":
			#フルパス分解 path:パス name:ファイル名 extention:拡張子
			pathSplit = re.search("(?P<path>^.*\/)(?P<name>.*?)\.(?P<extention>.*$)",path)
			self.filePath = pathSplit.group("path")
			self.fileName = pathSplit.group("name")
			self.fileExtention = pathSplit.group("extention")
		else:
			#ファイル名分解 name:ファイル名 extention
			pathSplit = re.search("(?P<name>.*?)\.(?P<extention>.*$)",path)
			self.fileName = pathSplit.group("name")
			self.fileExtention = pathSplit.group("extention")

	"""ファイル開いて二次配列にマッピング"""
	def crossMapping(self,path):
		try:
			with open(path , mode = "rt" , encoding = "utf-8" ) as file:
				if self.fileExtention == "csv" :
					readFile = pandas.read_csv(file , header = self.headLine , index_col = self.indexLine )

				self.crossMapOrigin = readFile
				self.crossMapAvatar = readFile
		except IndexError as e:
			print("入力されたファイルは存在しません")
		except IOError as e:
			print("指定されたファイルは開けません")
		else:
			pass
		finally:
			pass
		

	"""登録された関数の実行"""
	def commandCall(self , name , options = None):
		package = "Command"
		try:
			mod = importlib.import_module(name,package)
			commandClass = getattr(mod,name)
			commandObj = commandClass(self.crossMapOrigin , options)
			commandObj.execute()
		except ModuleNotFoundError as e:
			print(e)
			print("入力されたコマンドは存在しません")
		else:
			pass
		finally:
			pass

	def commandHelp(self, options = None):
		package = "./CMS/Command/"
		classList = []
		classHelpList = []
		docResult = []
		try:
			commandFile = os.listdir("./CMS/Command/")
			regePy = re.compile("(?!.*(__init__\.py|CrossMapCommand\.py))(?P<fname>.*)(\.py)")
			nameList = []
			for x in commandFile: 
				m = ""
				if regePy.match(x):
					m = regePy.match(x)
					m = m.group("fname")
					nameList.append(m)
			for x in nameList:
				# モジュールとして読み込み
				mod = importlib.import_module(x)
				commandClass = getattr(mod,x)
				callObj = commandClass()
				docResult.append(callObj.__doc__)
			for x in docResult:
				print(x)
		except ModuleNotFoundError as e:
			print(e)
			print("help失敗")
		else:
			pass
		finally:
			pass