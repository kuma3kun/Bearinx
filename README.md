# Bearinx
## Python数学ライブラリ資源利用用モジュール
CSVやTSVなど二次表をpandas・numpyを利用できるように変換・操作できるようにする仲介モジュール

### 予定
<dl>
<dt>コマンド一覧取得機能追加</dt>
<dd>コマンドのサブクラス一覧と、docstring取得してHelp生成する。</dd>
<dt>pandas用データ・numpy用データ変換機能追加</dt>
<dd>処理に応じてデータを変換する機能。
処理前の表を文字列型で保持しておいて処理後に比較することで、
データの損失を補完する？（文字列をstringからintにする際にNaNになるので）</dd>
<dt>インターフェース作成</dt>
<dd>CUIアプリとして作成しているが、他システムからCSVデータ、
コマンド文字列送信などで利用できるようにインターフェースの作成。</dd>
<dt>GUI化</dt>
<dd>インターフェース作成後、それを利用してExcelライクなUIを作成する。</dd>
<dd>Jupyter notebookが利用できるかも？</dd>
</dl>


-Bearinxインターフェース
各プログラムへのインターフェースを提供
単体でもCUIとして使えるように
	-CrossMapService
	二次元表操作ライブラリ
		-CrossMapCommand
		表操作コマンドをまとめる
		-CrossMapConveter
		Dataflame・ndarrayなどの型変換
	-CrossMapDB
	DBアクセス用ライブラリ
		-CMDQuery
		SQL文を渡すことでDB操作
		-CMDCommand
		DBアクセス用処理をまとめる
	-CrossMapGit
	2次元表データをCSVなどでgit管理する。
	これにより元に戻す操作などに利用する。
		-CMGCommand
		git操作用処理をまとめる
	-JointMapService
	二次元表を複数使用する操作用ライブラリ
	（表比較やマッチング結合や三次元表化など）
	-BearinxMacro
	Bearinx内で各コマンドをまとめたコマンド用ライブラリ
		-BMCommand
		各コマンドを連続して使用する処理をまとめる
		-BMRecorder
		画面の方で一連の操作のログを取ることで、
		BMCommandを生成する