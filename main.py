from bs4 import BeautifulSoup
import os
import modules.arg as arg
import modules.func as func

cmd = arg.CmdArg()

path: str = cmd.args.filename
only: str = cmd.args.only
exclude: list[str] = cmd.args.exclude
notab: bool = cmd.args.notab

with open(path, encoding='utf-8') as f:
  str = f.read()

basename = os.path.basename(path)
filename = os.path.splitext(basename)[0]

outputdir = "./output/"

if cmd.args.leave:
  output_name = filename + '.md'
else:
  output_name = cmd.args.output

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

meslist = list(filter(lambda m: m[2] != '', meslist))  # 発言が空ならスキップ

for m in meslist:
  tab = m[0]  # タブ名
  name = m[1]  # 名前
  mention = m[2]  # 発言
  if only is not None and only not in tab:
    continue
  if exclude is not None and tab in exclude:
    continue
  if name == '':  # 名前が空だったときの処理
    name = ' '
  out += func.makeoutstr(tab, name, mention, notab)

if not os.path.exists(outputdir):
  os.mkdir(outputdir)

with open(outputdir+output_name, mode='w', encoding='utf-8') as f:
  f.write(out)
