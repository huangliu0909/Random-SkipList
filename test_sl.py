import random
import datetime
import sys

minint = 0
maxint = sys.maxsize


class Node(object):
    def __init__(self, key=minint, value=[], level=1):
        self.key = key
        self.value = value
        self.level = level
        self.right = None
        self.down = None


class SkipList(object):
    def __init__(self):
        # 初始化层数和这一层的节点数
        self.top = Node(minint)
        self.top.left = None
        self.top.right = Node(maxint)
        self.top.right.left = self.top

    def findNode(self, key):
        return self.searchNode(self.top, key)

    def searchNode(self, node, key):
        while key >= node.right.key:
            node = node.right
        if key == node.key:
            return node
        if node.down is None:
            return None
        return self.searchNode(node.down, key)

    def insertNode(self, top, key, value):
        while key >= top.right.key:
            top = top.right
        if key == top.key:
            return None
        if top.down is None:
            node = Node(key, value)
            node.right = top.right
            top.right = node
            node.level = top.level
            return node
        downnode = self.insertNode(top.down, key, value)
        if downnode is not None:
            node = Node(key, value)
            node.right = top.right
            top.right = node
            node.down = downnode
            node.level = top.level
            return node
        return None

    def insert(self, key, value):

        k = self.getK()
        # 初始化现有最高点的level到新的level之间的链表
        for e in range(self.top.level + 1, k + 1):
            topleft = Node(minint, level=e)
            topright = Node(maxint, level=e)
            topleft.right = topright
            topleft.down = self.top
            self.top = topleft
        top = self.top
        while top.level != k:
            top = top.down
        self.insertNode(top, key, value)

    def getK(self):
        k = 1
        while random.randint(0, 100) > 50:
            k = k + 1
        return k

    def update_node(self, key, value):
        if self.findNode(key) is not None:
            self.findNode(key).value.append(value)
        else:
            l = []
            l.append(value)
            self.insert(key, l)

    def delete(self, key):
        node = self.top
        flag = 0
        while node is not None:
            while key >= node.right.key:
                former = node
                node = node.right
            if key == node.key:
                print("find delete")
                # print(former.right.key)
                search_node = node
                flag = 1
                break
            node = node.down
        if flag == 0:
            print("delete not found")
            return None
        while search_node is not None:
            """
            print("level")
            print(search_node.level)
            print("now")
            print(search_node.key)
            print(search_node.right.key)
            print(search_node.level)
            print("former")
            print(former.key)
            print(former.right.key)
            print(former.level)
            print("right")
            print(search_node.right.key)
            print(search_node.right.right.key)
            """
            former.right = search_node.right
            search_node = search_node.down
            former = former.down

    def searchByRange(self, k1, k2):
        result = []
        while self.findNode(k1) is None:
            k1 = k1 + 1
        node = self.findNode(k1)
        while node is not None:
            result.append(node.value)
            if node.right.key >k2:
                break
            node = node.right
        return result


if __name__ == '__main__':
    start = datetime.datetime.now()
    filename = "linux_distinct.txt"
    skiplist = SkipList()
    flag = 0
    with open(filename, "rb") as f:
        for fLine in f:
            flag += 1
            s = fLine.decode().strip().replace("\n", "").split(" ")
            collection = int(s[0])
            num = int(s[1])
            skiplist.update_node(num, collection)
    end = datetime.datetime.now()
    print("建立时间：" + str((end - start)))

    start = datetime.datetime.now()
    print(skiplist.findNode(2148).value)
    end = datetime.datetime.now()
    print("查询时间：" + str((end - start)))

    start = datetime.datetime.now()
    skiplist.delete(2148)
    end = datetime.datetime.now()
    print("删除时间：" + str((end - start)))
    print("删除后： " + str(skiplist.findNode(2148)))


    l = []
    l.append(777)
    skiplist.insert(2148, l)
    print("插入后： " + str(skiplist.findNode(2148).value))
    start = datetime.datetime.now()
    skiplist.update_node(2148, 888)
    end = datetime.datetime.now()
    print("更新结点时间：" + str((end - start)))
    print("更新后： " + str(skiplist.findNode(2148).value))
    start = datetime.datetime.now()
    print(skiplist.searchByRange(1, 10))
    end = datetime.datetime.now()
    print("区间查询结点时间：" + str((end - start)))