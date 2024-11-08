import re

pattern = r'\W+'

text = 'This is string! Yes, this is string. And 123 is number.'

x = re.findall(pattern, text)

print(x)