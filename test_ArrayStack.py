import unittest
import ArrayStack

class TestArrayStack(unittest.TestCase):

    def test_add(self):
        stack = ArrayStack.ArrayStack()
        stack.push(1)
        result = stack.size()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()