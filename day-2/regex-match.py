import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
  print("Found the match:", match.group())
else:
  print("No match found.")

