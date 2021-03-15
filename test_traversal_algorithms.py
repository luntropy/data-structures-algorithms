#!/usr/bin/python3

import io
import unittest
import unittest.mock

from data_structures import graph
from data_structures import binary_tree as bt

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.g = graph.Graph()

        self.g.add_edge(0, 1)
        self.g.add_edge(0, 2)
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 0)
        self.g.add_edge(2, 3)
        self.g.add_edge(3, 3)

        self.root = bt.Node()

        self.root.insert(2)
        self.root.insert(0)
        self.root.insert(1)
        self.root.insert(-1)
        self.root.insert(3)
        self.root.insert(4)
        self.root.insert(5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_dfs(self, n, expected_output, mock_stdout):
        self.g.dfs(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_dfs(self):
        self.assert_stdout_dfs(0, '0 1 2 3 ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_dfs_stack(self, n, expected_output, mock_stdout):
        self.g.dfs_stack(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_dfs_stack(self):
        self.assert_stdout_dfs_stack(0, '0 2 3 1 ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_bfs(self, n, expected_output, mock_stdout):
            self.g.bfs(n)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_bfs(self):
        self.assert_stdout_bfs(0, '0 1 2 3 ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_preorder(self, expected_output, mock_stdout):
            self.root.preorder()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_preorder(self):
        self.assert_stdout_preorder('2 0 -1 1 3 4 5 ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_inorder(self, expected_output, mock_stdout):
            self.root.inorder()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_inorder(self):
        self.assert_stdout_inorder('-1 0 1 2 3 4 5 ')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_postorder(self, expected_output, mock_stdout):
            self.root.postorder()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_postorder(self):
        self.assert_stdout_postorder('-1 1 0 5 4 3 2 ')

if __name__ == '__main__':
    unittest.main()
