from bs4 import BeautifulSoup
import os
import re


class Convert():

    def __init__(self,
                 path: str, output_name: str,
                 output_dir: str,
                 excludes: list[str],
                 is_only: bool, is_leave: bool, is_notab: bool):
        with open(path, encoding='utf-8') as f:
            str = f.read()

        basename = os.path.basename(path)
        filename = os.path.splitext(basename)[0]

        self.meslist = list()
        self.output_dir = output_dir
        self.excludes = excludes
        self.is_only = is_only
        self.is_leave = is_leave
        self.is_notab = is_notab
        self.output_name = output_name
        self.output_name = filename + '.md' if self.is_leave else self.output_name

        self.out = f"# {os.path.splitext(self.output_name)[0]}\n\n"
        self.soup = BeautifulSoup(str, 'html.parser')

    def _search_and_get(self):
        messages = self.soup.find_all('p')
        get_inner_slice = slice(1, -1)
        for msg in messages:
            tmplist = list()
            for span in msg.find_all('span'):
                if span is None:
                    s = ''
                else:
                    s = str(span)
                s = re.sub(r'</?span>', '',
                           s.replace('<br/>', '\n')).strip()
                if '#' in s:
                    s = s.replace('#', '\\#')
                tmplist.append(s)
            tmplist[0] = tmplist[0][get_inner_slice]  # タブ名の[]の内側の文字列を取得
            self.meslist.append(tmplist)

    def _make_outstr(self):
        # 発言が空ならスキップ
        self.meslist = list(
            filter(lambda m: m[2] != '', self.meslist))
        for m in self.meslist:
            tab = m[0]  # タブ名
            name = m[1]  # 名前
            mention = m[2]  # 発言
            if self.is_only is not None and self.is_only not in tab:
                continue
            if self.excludes is not None and tab in self.excludes:
                continue
            if name == '':  # 名前が空だったときの処理
                name = ' '
            self.out += self._make_linestr(tab, name, mention, self.is_notab)

    def _out_file(self):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        with open(self.output_dir+self.output_name, mode='w', encoding='utf-8') as f:
            f.write(self.out)

    def _make_linestr(self, tab: str, name: str,
                 mention: str, is_notab=False,
                 blacket=('【', '】'), em='**') -> str:
        if is_notab:
            return f"{em}{name}{em} : {mention}\n\n"
        else:
            return f"{blacket[0]}{tab}{blacket[1]} {em}{name}{em} : {mention}\n\n"

    def run(self):
        self._search_and_get()
        self._make_outstr()
        self._out_file()


def main(path, output_name='out.md', output_dir='./output/',
         exclude=None, only=None, leave=False, notab=False):
    apcv = Convert(path, output_name, output_dir,
                   exclude, only, leave, notab)
    apcv.run()
