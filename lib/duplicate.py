def duplicate(string):
  lower_case = string.lower()
  array = list(lower_case)
  encoded = []

  for c in array:
    if len(array) > 1 and array.count(c) > 1:
      encoded.append(')')
    else:
      encoded.append('(')

  return ''.join(encoded)
