from bs4 import BeautifulSoup
import os
import modules.arg as arg

cmd = arg.CmdArg()

path = cmd.args.filename
only = cmd.args.only
exclude = cmd.args.exclude

with open(path, encoding='utf-8') as f:
  str = f.read()

basename = os.path.basename(path)
filename = os.path.splitext(basename)[0]

if cmd.args.leave:
  output = filename+'.md'
else:
  output = cmd.args.output

soup = BeautifulSoup(str, 'html.parser')
messages = soup.find_all('p')
meslist = []
get_inner = slice(1, -1)
for msg in messages:
  inlist = []
  for span in msg.find_all('span'):
    str = span.string
    if str is not None:
      str = str.strip()
    else:
      str = ''
    if '#' in str:
      str = str.replace('#', '\\#')
    inlist.append(str)
  inlist[0] = inlist[0][get_inner]
  meslist.append(inlist)

out = f"# {filename}\n\n"

for m in meslist:
  tab = m[0]  # タブ名
  name = '**'+m[1]+'**'  # 名前
  mention = m[2]  # 発言
  exFlag = False
  if mention == '': #発言が空ならスキップ
    continue
  if name == '****': #名前が空だったときの処理
    name = ' '
  if only is not None and only in tab:
    continue
  if exclude is not None and tab in exclude:
    continue
  out += f"【{tab}】 {name} : {mention}\n\n"

with open("./output/"+output, mode='w', encoding='utf-8') as f:
  f.write(out)
