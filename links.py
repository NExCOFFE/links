with open('links1.txt', 'r', encoding='utf-8') as f1:
    text = f1.read().splitlines()
    # text = set(text)


with open('links2.txt', 'r', encoding='utf-8') as f2:
    text2 = f2.read().splitlines()
    # text2 = set(text2)
# match_links = text.intersection(text2)
# print(match_links)
match_links = []
unmatch_links = []
for i in text2:
    if i in text or i.replace("!", "") in text:
        match_links.append(i.replace('!',''))
    else:
        unmatch_links.append(i)
for i in text:
    if i not in match_links or i.replace('!','') not in match_links:
        unmatch_links.append(i)
print(match_links)
print(unmatch_links)

with open('mathc_links.txt', 'w', encoding='utf-8')as f:
    f.write('\n'.join(match_links))


with open('unmatch_links.txt', 'w', encoding='utf-8')as f:
    f.write('\n'.join(unmatch_links))