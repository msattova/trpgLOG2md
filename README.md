# trpgLOG2md

HTMLファイル形式で出力されたTRPGのログをマークダウン形式に変換するプログラムです。

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/msattova/trpgLOG2md)

**現在、ccforiaから出力されたログに対してのみ動作確認を行っております。**

他オンラインセッションツールについては今後対応予定です。

※本プログラムは作者が個人的に制作したものであり、オンラインセッションツール等とは一切の関係がありません。

## 使い方

```log
usage: main.py [-h] [-l] [-o [OUTPUT]] [--only ONLY] [--exclude [EXCLUDE ...]] [--notab] filename

HTMLファイル形式のTRPGログをmarkdownにするツールです。

positional arguments:
  filename              変換したいログのファイル名

options:
  -h, --help            show this help message and exit
  -l, --leave           出力ファイル名を入力ファイル名と同じにする （-oオプションは無視されます）
  -o [OUTPUT], --output [OUTPUT]
                        出力ファイル名
  --only ONLY           指定したタブのみ変換
  --exclude [EXCLUDE ...]
                        指定したタブを除外して変換
  --notab               タブ名を表示しない
```

## TODO

- [ ] 文字色を残すオプションの追加（markdown記法では無理なのでHTMLタグとして実装予定）
- [ ] HUGOショートコードを含めるオプションの追加（HUGO利用者以外には恩恵はありません。ほぼ自分用）

（適宜追記予定）
