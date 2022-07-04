s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s = s.split()
d = dict({el: s.count(el) for el in s})
dd = {}
for key, value in sorted(d.items(), key=lambda x: (x[0], x[1])):
    dd[key] = value
l_num = list(dd.values())
indx = l_num.index(max(l_num))
print(list(dd.keys())[indx])
