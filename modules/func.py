
def makeoutstr(tab: str, name: str, mention: str, is_notab=False, blacket=('【','】'), em='**')->str:
  if is_notab:
    return f"{em}{name}{em} : {mention}\n\n"
  else:
    return f"{blacket[0]}{tab}{blacket[1]} {em}{name}{em} : {mention}\n\n"
