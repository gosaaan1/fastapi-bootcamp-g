# fastapi-bootcamp
[FastAPI](https://fastapi.tiangolo.com/)ブートキャンプ

## 依存するパッケージのインストール
```bash
pip install -r requirements.txt
```
## データベースマイグレーション
```bash
alembic upgrade head
```

## SQLiteデータベースの操作

+ アクティビティバーからデータベースを選択
+ Create Connectionを選択
+ Server TypeでSQLiteを選択
+ SQLite DB Pathでtodo.dbを選択
+ Saveボタンを押下し保存する
+ テーブル構造などを確認する

## サーバーの立ち上げ

+ コマンドバレットから **サーバー起動(デバッグ)** タスクを実行
+ 新しく **サーバー起動(デバッグ)** のターミナルが開始されたのを確認

## VisualStudio Codeでのデバッグ方法

+ 実行とデバッグで **デバッグ(アタッチ)** を選択し開始

## サーバーの停止

+ **サーバー起動(デバッグ)** のターミナルでCtrl+Cで停止させる。（デバッグも停止する）

## Web APIのリクエスト

+ アクティビティバーから[Thunder Client](https://www.thunderclient.com/)を選択
+ CollectionsタブのハンバーガーメニューからImportを選択
+ tool/thunder-client/thunder-collection_fastapi-bootcamp.jsonを読み込む

## ログ出力の確認

+ ORMが生成しているSQLのログを確認する
+ リクエストのログを確認する

