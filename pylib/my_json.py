import json
text = "{\"text\":[\"cccc\",\"bbb\",\"aa\"] , \"link\":[\"aaaa\",\"cc\",\"b\"] } "
jsob = json.loads(text)
print('load json: ', jsob)
print('   text: ', jsob['text'])
print('   text[0]: ', jsob['text'][0])