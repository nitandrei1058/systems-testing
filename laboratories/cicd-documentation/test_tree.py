import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

    def test_find_existing_node(self):
        node = self.tree.find(4)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_non_existing_node(self):
        node = self.tree.find(10)
        self.assertIsNone(node)

    def test_find_root_node(self):
        node = self.tree.find(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

if __name__ == '__main__':
    unittest.main()
