import re

text = "apples, grapes, oranges, mango"

pattern = r","

split_result = re.split(pattern, text)
print("Split Result:", split_result)
