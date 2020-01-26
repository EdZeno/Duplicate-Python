def duplicate(string):
  a = list(string)
  if len(a) > 1 and a[0] == a[1]:
    return ')'
  else:
    return '('
