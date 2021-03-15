#!/usr/bin/python3

# Part of DFS
# TC: O(b^m), SC: O(b * m)
def dfs_until(v, visited, graph):
    visited.add(v)
    print(v, end = ' ')

    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs_until(neighbour, visited, graph)

def dfs(graph, s):
    visited = set()
    dfs_until(s, visited, graph)

def dfs_stack(graph, s):
    visited = set()
    stack = []

    stack.append(s)

    while stack:
        v = stack.pop()

        if v not in visited:
            print(v, end = ' ')
            visited.add(v)

            for c in graph[v]:
                stack.append(c)

# TC: O(b^(d + 1)), SC: O(b^(d + 1))
def bfs(graph, s):
    visited = set()
    queue = []

    queue.append(s)

    while queue:
        v = queue.pop(0)

        if v not in visited:
            print(v, end = ' ')
            visited.add(v)

            for c in graph[v]:
                queue.append(c)

def preorder(root):
    if root:
        print(root.value, end = ' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end = ' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end = ' ')
