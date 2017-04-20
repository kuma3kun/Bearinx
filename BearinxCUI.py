import pandas
from BearinxInterface import BearinxInterface

"""
BearinxCUI
"""
class BearinxCUI:
	SYS_HEAD = "CrMp>"
	fullPath = ""
	headLine = None
	indexLine = None

	def __init__(self,path,headLine = None,indexLine = None):
		self.fullPath = path
		self.headLine = headLine
		self.indexLine = indexLine

	"""CUI操作用"""
	def start(self):
		inter = BearinxInterface()
		cms = inter.cmsPathOpen(self.fullPath,self.headLine,self.indexLine)
		endFlag = 0
		while endFlag == 0 :
			print( self.SYS_HEAD + "コマンド入力してください（list:関数一覧表示 desc:現在の配列確認 write:書き出し end:終了）" )
			command = input(self.SYS_HEAD)

			if command == "desc":
				inter.cmsDesc(cms)
			elif command == "end":
				endFlag = 1
			elif command != "":
				inter.cmsCommandCall(cms,command)
			else :
				print(command)

if __name__ == "__main__":
	print("ファイルパスを入力してください")
	inputPath = input()
	print("列名付き？ Yes=1 No=0")
	inputHeadLine = input()
	print("行番号付き？ Yes=1 No=0")
	inputIndexLine = input()

	obj = BearinxCUI(inputPath,inputHeadLine,inputIndexLine)
	obj.start()