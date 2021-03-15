#!/usr/bin/python3

import sys
sys.path.append('../')
from algorithms import traversal_algorithms as trav_alg

class Node:
    def __init__(self, key = None):
        if key == None:
            self.value = None
        else:
            self.value = key

        self.left = None
        self.right = None

    def add_left_node(self, key):
        node = Node(key)
        self.left = node

        return node

    def add_right_node(self, key):
        node = Node(key)
        self.right = node

        return node

    def insert(self, key):
        if self.value != None:
            if key < self.value:
                if not self.left:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.value:
                if not self.right:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.value = key

    def min_value_node(self):
        current = self

        while current.left != None:
            current = current.left

        return current

    def delete(self, key):
        if key < self.value and self.left:
            self.left = self.left.delete(key)
        elif key > self.value and self.right:
            self.right = self.right.delete(key)
        else:
            if self.left == None:
                temp = self.right
                self = None
                return temp
            elif self.right == None:
                temp = self.left
                self = None
                return temp
            else:
                temp = self.right.min_value_node()

                self.value = temp.value
                self.right = self.right.delete(key)

        return self

    def search(self, key):
        if self.value == key:
            return self
        elif key < self.value and self.left:
            return self.left.search(key)
        elif key > self.value and self.right:
            return self.right.search(key)
        else:
            return None

    def preorder(self):
        trav_alg.preorder(self)

    def inorder(self):
        trav_alg.inorder(self)

    def postorder(self):
        trav_alg.postorder(self)

if __name__ == '__main__':
    root = Node()

    root.insert(2)
    root.insert(0)
    root.insert(1)
    root.insert(-1)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    print('Binary tree: ')
    root.inorder()
    print()

    x = 2
    print()
    print('Searching for x = {0}: '.format(x))
    res_node = root.search(x)
    if res_node:
        print(res_node.value)
    else:
        print(res_node)

    print()
    print('Deleting x = {0}..'.format(x))
    root.delete(2)

    print()
    print('Result after deletion: ')
    root.inorder()
    print()

    print()
    print('Searching for x = {0}: '.format(x))
    res_node = root.search(x)
    if res_node:
        print(res_node.value)
    else:
        print(res_node)

    print()
    print('Preorder traversal: ')
    root.preorder()
    print()

    print('Inorder traversal: ')
    root.inorder()
    print()

    print('Postorder traversal: ')
    root.postorder()
    print()
