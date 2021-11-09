li = []
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data, node):
        if data >= node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                node.right.insert(data, node.right)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                node.left.insert(data, node.left)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data,self.root)
        return self.root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def tranToList(self, node):
        global li
        if node is not None:
            li.append(node.data)
            self.tranToList(node.left)
            self.tranToList(node.right)
        li.sort()
        return li

    def checkRank(self, key):
        listT = self.tranToList(self.root)
        for i in range(0, len(listT)):
            if key < listT[i]:
                return i
            if i == len(listT)-1 and key > listT[i]:
                return len(listT)


T = BST()
inp,key = input('Enter Input : ').split('/')
ip = [int(i) for i in inp.split()]
for i in ip:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(f'Rank of {key} : {T.checkRank(int(key))}')
