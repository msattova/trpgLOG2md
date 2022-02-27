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
            code = f.read()

        basename = os.path.basename(path)
        filename = os.path.splitext(basename)[0]

        self.msglist = list()
        self.output_dir = output_dir
        self.excludes = excludes
        self.is_only = is_only
        self.is_leave = is_leave
        self.is_notab = is_notab
        self.output_name = output_name
        self.output_name = filename + '.md' if self.is_leave else self.output_name

        self.out_str = f"# {os.path.splitext(self.output_name)[0]}\n\n"
        self.soup = BeautifulSoup(code, 'html.parser')

    def _search_and_get(self, soup) -> list[str]:
        msglist = list()
        messages = soup.find_all('p')
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
            msglist.append(tmplist)
        return msglist

    def _make_outstr(self, msglist: list[str]) -> str:
        out = ''
        # 発言が空ならスキップ
        messages = list(
            filter(lambda m: m[2] != '', msglist))
        for m in messages:
            tab = m[0]  # タブ名
            name = m[1]  # 名前
            mention = m[2]  # 発言
            if self.is_only is not None and self.is_only not in tab:
                continue
            if self.excludes is not None and tab in self.excludes:
                continue
            if name == '':  # 名前が空だったときの処理
                name = ' '
            out += self._make_linestr(tab, name, mention, self.is_notab)
        return out

    def _out_file(self, output_dir: str, output_name: str, out_str: str):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        with open(output_dir+output_name, mode='w', encoding='utf-8') as f:
            f.write(out_str)

    def _make_linestr(self, tab: str, name: str,
                      mention: str, is_notab=False,
                      blacket=('【', '】'), em='**') -> str:
        if is_notab:
            return f"{em}{name}{em} : {mention}\n\n"
        else:
            return f"{blacket[0]}{tab}{blacket[1]} {em}{name}{em} : {mention}\n\n"

    def run(self):
        self.msglist = self._search_and_get(self.soup)
        self.out_str += self._make_outstr(self.msglist)
        self._out_file(self.output_dir, self.output_name, self.out_str)


def main(path, output_name='out.md', output_dir='./output/',
         exclude=None, only=None, leave=False, notab=False):
    apcv = Convert(path, output_name, output_dir,
                   exclude, only, leave, notab)
    apcv.run()

