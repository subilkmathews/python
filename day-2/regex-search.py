import re

text = "The brown quick fox"

pattern =r"quick"

search = re.search(pattern, text)

if search:
   print("pattern found:", search.group())
else:
  print("not found")

