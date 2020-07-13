dic = {"Kim":"75", "Hong":"90", "Choi":"88", "Lee":"72"}

data = sorted(dic.items(), key = lambda item: item[1])
print("오름차순 정렬")
for key, value in data:
     print( key, ":", value)

data1 = sorted(dic.items(), reverse = True, key = lambda item: item[1])
print("내림차순 정렬")
for key, value in data1:
     print(key, ":", value)

