# dictSorted.py
wordInfo = {'세탁기' : 50, '선풍기' : 30, '청소기' : 40, '냉장고' : 60}
print(('# 키에 대하여 역순으로 정리하기'))
reverse_key = sorted(wordInfo.keys(), reverse=True)
print(reverse_key)

print(('# 값을 기반으로 역순으로 정리하기'))
reverse_values = sorted(wordInfo.values(), reverse=True)
print(reverse_values)

print(('# 값을 기반으로 키를 역순으로 정리하기'))
myticks = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(myticks)