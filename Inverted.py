import datetime
# 每行形如“i,j”，表明第i个集合包含了元素j
start = datetime.datetime.now()
filename = "linux_distinct.txt"
#filename = "AOL_out.txt"
x = 0
flag = 0
inverted_map = {}
with open(filename, "rb") as f:
    for fLine in f:
        s = fLine.decode().strip().replace("\n", "").replace(" ", "\t").split("\t")
        # print(s)
        collection = s[0]
        num = s[1]
        if num not in inverted_map.keys():
            l = []
            l.append(collection)
            inverted_map[num] = l
        else:
            # if collection not in inverted_map[num]:
                inverted_map[num].append(collection)
end = datetime.datetime.now()
print("建立时间：" + str((end - start)))
start = datetime.datetime.now()
print(inverted_map["2148"])
end = datetime.datetime.now()
print("查询时间：" + str((end - start)))


def inverted_delete(map, c, n):
    if n in map.keys():
        map[n].remove(c)


start = datetime.datetime.now()
inverted_delete(inverted_map, "1", "1")
# print("删除时间：" + str((end - start)))

# print(inverted_map["1"])


def inverted_insert(map, c, n):
    if n in map.keys():
        if c not in map[n]:
            map[n].append(c)
    else:
        l = []
        l.append(c)
        map[n] = l


start = datetime.datetime.now()
inverted_insert(inverted_map, "9", "1")
end = datetime.datetime.now()
print("插入时间：" + str((end - start)))

print(inverted_map["1"])