import json
# text = "{\"text\":[\"cccc\",\"bbb\",\"aa\"] , \"link\":[\"aaaa\",\"cc\",\"b\"] } "
# jsob = json.loads(text)
# print(jsob)


text2 = "[['aa','bb','cc',['11','22']],['dd','ee','ff',['3333','44444']],[['gg','hhh','iiii',['5555','6666']]]]"
obj2 = json.loads(text2)
print(obj2)