import re


html_code = input()

regex = r'<title>(.*)<\/title>|<body>(.*)<\/body>'

matches = re.findall(regex, html_code)
content = re.sub(r'<\/?.*?>|\\n','',matches[1][1])

print(f'Title: {matches[0][0]}')
print(f'Content: {content}')
