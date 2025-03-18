import re


links_list = []
regex = r'((www)\.[A-Za-z0-9\-]+(\.[a-z]+)+)'


while True:
    text = input()
    if not text:
        break

    link = re.search(regex, text)
    if link:
        links_list.append(link.group(1))

for link in links_list:
    print(link)

