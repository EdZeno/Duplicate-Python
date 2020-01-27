def duplicate(string):
  a = list(string)
  string1 = ""

  for c in a:
    print(a)
    print(c)
    print(string1)
    if len(a) > 1 and a[0] == a[1]:
      string1 + '))'
    else:
      string1 + '('
