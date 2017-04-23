from CrossMapCommand import CrossMapCommand

"""
二次元表操作処理
合計値算出
"""
class Sum(CrossMapCommand) :
	"""
	Sum:合計値算出
	@t：加算タイプ
		-cell：セル単位
		-col:横一列
		-row:縦一列
		-all：全体
	"""
	SYS_HEAD = "CMC>"
	#処理対象の表データ型
	MAP_TYPE = "pandas"
	#処理対象の表内データ型
	DATA_TYPE = "DataFrame"
	crossMap = ""
	options = None

	def __init__(self,map = None,options = None):
		self.crossMap = map
		self.options = options

	"""関数の実行"""
	def execute(self):
		print("SUM関数実行")
		self.optionRead()

		return map

	def optionRead(self):
		print(self.options)