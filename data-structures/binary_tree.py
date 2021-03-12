#!/usr/bin/python3

import sys
sys.path.append('../algorithms/')
import algorithms as alg

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def add_left_node(self, key):
        node = Node(key)
        self.left = node

        return node

    def add_right_node(self, key):
        node = Node(key)
        self.right = node

        return node

    def preorder(self):
        alg.preorder(self)

    def inorder(self):
        alg.inorder(self)

    def postorder(self):
        alg.postorder(self)

if __name__ == '__main__':
    root = Node(1)
    rl = root.add_left_node(2)
    rr = root.add_right_node(3)
    rll = rl.add_left_node(4)
    rlr = rl.add_right_node(5)

    print('Preorder traversal: ')
    root.preorder()

    print()
    print('Inorder traversal: ')
    root.inorder()

    print()
    print('Postorder traversal: ')
    root.postorder()
    print()
