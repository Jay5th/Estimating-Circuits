import unittest
from BooleanCircuits.BinaryOperation import BinaryOperation


class TestBinaryOperation(unittest.TestCase):
    def test_zero(self):
        zero = BinaryOperation(name='zero')
        for a in (0, 1):
            for b in (0, 1):
                self.assertEqual(0, zero(a, b)), f"failed 'zero' test"

    def test_one(self):
        one = BinaryOperation(name='one')
        for a in (0, 1):
            for b in (0, 1):
                self.assertEqual(1, one(a, b)), "input failed 'one' test"

    def test_and(self):
        and_op = BinaryOperation(name='and')
        for a in (0, 1):
            for b in (0, 1):
                self.assertEqual(a & b, and_op(a, b)), f"failed 'and' test"

    def test_or(self):
        or_op = BinaryOperation(name='or')
        for a in (0, 1):
            for b in (0, 1):
                self.assertEqual(a | b, or_op(a, b)), f"failed 'or' test"

    def test_xor(self):
        xor = BinaryOperation(name='xor')
        for a in (0, 1):
            for b in (0, 1):
                self.assertEqual(a ^ b, xor(a, b)), f"failed 'xor' test"


if __name__ == '__main__':
    unittest.main()
