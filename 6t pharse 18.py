import re
def multiple (patterns, string):
  for i in patterns:
    if not re.search(i, string):
      return False
  
  if 6 <= len(string) <= 12:
    return True
  else:
    return False
x = str(input("Type password: "))
patterns = [r"[a-z]", r"[A-Z]", r"[0-9]", r"[$|#|@]"]
print(multiple(patterns, x))



