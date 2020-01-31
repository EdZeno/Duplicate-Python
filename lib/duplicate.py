def duplicate(string):
  lower_case = string.lower()
  a = list(lower_case)
  string1 = []

  for c in a:

    print(a)
    print(c)
    print(string1)
    if len(a) > 1 and a.count(c) > 1:
      string1.append(')')
    else:
      string1.append('(')

  return ''.join(string1)
