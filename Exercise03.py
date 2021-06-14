# Given the root to a binary tree,
# implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
# def init(self, val, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def serialize(self):
        node_string = str(self.value)
        if self.left is not None:
            node_string += "/" + self.left.serialize()
        if self.right is not None:
            node_string += "/" + self.right.serializa()
        return node_string


print(Node(1, Node("l2", None, None), None).serialize())
