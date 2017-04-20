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


- BearinxCUI
	- BearinxInterface
		- CrossMapService
			- CrossMapCommand
			- CrossMapConverter
		- CrossMapSQL
			- CMDQuery
			- CMDCommand
		- CrossMapGit
			- CMGCommand
		- JointMapService
			- JMSCommand
		- BearinxMacro
		- BearinxMacroRecorder

<dl>
<dt>BearinxCUI</dt>
<dd>とりあえずCUIアプリとして完結できるようにテスト</dd>
</dl>
<dl>
<dt>Bearinxインターフェース</dt>
<dd>各プログラムへのインターフェースを提供</dd>
</dl>
<dl>
<dt>CrossMapService</dt>
<dd>二次元表操作ライブラリ</dd>
<dt>CrossMapCommand</dt>
<dd>表操作コマンドをまとめる</dd>
<dt>CrossMapConveter</dt>
<dd>Dataflame・ndarrayなどの型変換</dd>
</dl>
<dl>
<dt>CrossMapSQL</dt>
<dd>DBアクセス用ライブラリ</dd>
<dt>CMDQuery</dt>
<dd>SQL文を渡すことでDB操作</dd>
<dt>CMDCommand</dt>
<dd>DBアクセス用処理をまとめる</dd>
</dl>
<dl>
<dt>CrossMapGit</dt>
<dd>2次元表データをCSVなどでgit管理する。</dd>
<dd>これにより元に戻す操作などに利用する。</dd>
<dt>CMGCommand</dt>
<dd>git操作用処理をまとめる</dd>
</dl>
<dl>
<dt>JointMapService</dt>
<dd>二次元表を複数使用する操作用ライブラリ（表比較やマッチング結合や三次元表化など）</dd>
<dt>JMSCommand</dt>
<dd>二次元表複数操作処理をまとめる</dd>
</dl>
<dl>
<dt>BearinxMacro</dt>
<dd>Bearinx内で各コマンドをまとめたコマンド用ライブラリ</dd>
<dt>BMCommand</dt>
<dd>各コマンドを連続して使用する処理をまとめる</dd>
<dt>BMRecorder</dt>
<dd>画面の方で一連の操作のログを取ることで、BMCommandを生成する</dd>
</dl>