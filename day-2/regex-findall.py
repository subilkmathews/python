import re

text = "This is a quick brown fox"

pattern = r"brown"

search = re.search(pattern, text)

if search:
   print("Pattern found:", search.group())
else:
  print("Pattern not found")

