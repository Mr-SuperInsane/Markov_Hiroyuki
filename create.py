import markovify

with open('ひろゆきツイート.json', 'r', encoding='utf-8') as f:
    text_model = markovify.Text.from_json(f.read())

for i in range(10):
    print(text_model.make_short_sentence(140))