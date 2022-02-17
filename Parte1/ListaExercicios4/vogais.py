def vogal(l):
  if l.lower() in ('a', 'e', 'i', 'o', 'u'):
    return True
  elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
    return True
  else:
    return False