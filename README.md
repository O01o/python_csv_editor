# python-csv-editor

## 概要

CSVファイルについて、PySimpleGUIを使用して、横持ちのデータを縦持ちに変換するアプリを制作しました。

## 環境設定

今回は仮想環境のツールとして **Rye** を使用しています。

以下のコマンドを入力してください。

Pythonのバージョンは3.11にしています。現時点(2024/02/25時点)で Nuitka は Python 3.12 で動作しないことに注意してください。

<pre>
rye pin 3.11
rye add nuitka
rye add pysimplegui
rye add pandas
rye add <その他必要なパッケージ名>
rye sync
</pre>

Windowsアプリケーション(EXE)化するには、以下の一つのコマンドを入力してください。

<pre>
rye run python -m nuitka main.py --standalone --onefile --follow-imports --enable-plugin=numpy --enable-plugin=tk-inter --disable-console
</pre>

プロジェクト直下に main.exe が生成されます。
