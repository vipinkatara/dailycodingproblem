#This code is not working
class Node:
    s = ''
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        if root:
            serialize(root.left)
            self.s = self.s + root.val
            serialize(root.right)
        return s
    def deserialize(self, stri):
        s = iter(stri)
        tree = []
        for x in s:
            if x == "(":
                tree.append(subtrees(s))
            elif x == ")":
                return tree
            else:
                tree.append(int(x))
        return tree[0]


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

