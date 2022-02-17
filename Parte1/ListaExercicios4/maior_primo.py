def primo(x):
  prim = True
  i = 1
  while prim and i < (x-1):
    if x % (x - i) == 0:
      prim = False
    i += 1
  return prim
    
def maior_primo(x):
  if primo(x):
    return x
  else:
    while not primo(x):
      x -= 1
    return x