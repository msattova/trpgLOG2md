# trpgLOG2md

HTMLファイル形式で出力されたTRPGのログをマークダウン形式に変換するプログラムです。

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/msattova/trpgLOG2md)

オンラインセッションツールから出力されたログであっても、HTMLの構成によっては正常に動作しない場合があります。ご注意下さい。

**※本プログラムは作者が個人的に制作したものであり、オンラインセッションツール等とは一切の関係がありません。**

## 実行に必要なもの

versionの表記は動作確認した環境でのものになります。

* python : v3.10.1
* beautifulsoup4 : 4.10.0
* toml : 0.10.2 (`--setting`オプションを使わない場合は不要)

## 使い方

```log
usage: main.py [-h] [-l] [-o [OUTPUT]] [-d [OUTDIR]] [--only ONLY]
               [--excludes [EXCLUDES ...]] [--notab] [--blacket BLACKET]
               [--namedeco NAMEDECO] [-s SETTING]
               filename

HTMLファイル形式のTRPGログをmarkdownにするツールです。

positional arguments:
  filename              変換したいログのファイル名

options:
  -h, --help            show this help message and exit
  -l, --leave           出力ファイル名を入力ファイル名と同じにする （-oオプションは無視され
ます）
  -o [OUTPUT], --output [OUTPUT]
                        出力ファイル名
  -d [OUTDIR], --outdir [OUTDIR]
                        出力フォルダ名
  --only ONLY           指定したタブのみ変換
  --excludes [EXCLUDES ...]
                        指定したタブを除外して変換
  --notab               タブ名を表示しない
  --blacket BLACKET     タブ名を囲む括弧を設定（例：--blacket "【】"）
  --namedeco NAMEDECO   キャラの名前欄を囲むマークダウン装飾を設定（例： --namedeco "**"）
  -s SETTING, --setting SETTING
                        コマンド設定の記述されたtomlファイルを読み込みます（tomlファイルの設定が優先されます）
```

## TODO

- [ ] 文字色を残すオプションの追加（markdown記法では無理なのでHTMLタグとして実装予定）
- [ ] HUGOショートコードを含めるオプションの追加（HUGO利用者以外には恩恵はありません。ほぼ自分用）
* [ ] [この記事](https://qiita.com/msattova/items/8120b23f2470667af359)に書いた出力先ディレクトリを指定できない問題の解決

（適宜追記予定）
