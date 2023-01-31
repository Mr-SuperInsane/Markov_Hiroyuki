import markovify

text = open("ひろゆきツイート.txt", "r", encoding='utf-8').read()
text_model = markovify.NewlineText(text, state_size=3, well_formed=False)
with open('ひろゆきツイート.json', 'w', encoding='utf-8') as f:
    f.write(text_model.to_json())