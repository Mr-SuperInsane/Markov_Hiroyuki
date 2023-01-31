import MeCab
import re

text = open("ひろゆきツイート.txt","r",encoding='utf-8').read()
table = str.maketrans({
        # '\n': '',
        # '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
text = text.translate(table).split()
url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

for i in range(10):
    for line in text:
        if re.match(url_pattern, line): # URL
            text.remove(line)
        elif bool(re.search(r'[a-zA-Z0-9]', line)):
            text.remove(line)
        elif re.match('^@.*', line):
            text.remove(line)
        elif re.match('.*,$', line):
            text.remove(line)
        elif re.match('^#.*', line):
            text.remove(line)
        elif re.match('RT', line):
            text.remove(line)

m = MeCab.Tagger('-Owakati')
f = open('ひろゆきツイート.txt', 'w',encoding='utf-8')
for line in text:
    splited_line = m.parse(line)
    f.write(str(splited_line))
f.close()