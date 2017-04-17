from CrossMapCommand import CrossMapCommand

"""
二次元表操作処理
合計値算出
"""
class Sum(CrossMapCommand) :
	SYS_HEAD = "CMC>"
	#処理対象の表データ型
	MAP_TYPE = ""
	#処理対象の表内データ型
	DATA_TYPE = ""
	crossMap = ""

	def __init__(self,map,options = None):
		self.crossMap = map

	"""関数の実行"""
	def execute(self):
		print("SUM関数実行結果")
		return map

