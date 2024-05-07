import unittest
from BooleanCircuits.BinaryGate import BinaryGate
from BooleanCircuits.BinaryOperation import BinaryOperation


class TestBinaryGate(unittest.TestCase):
    def test_zero(self):
        data_input = (0, 1, 1)
        zero = BinaryOperation(name='zero')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                zero_gate = BinaryGate(indices=(i, j), operation=zero)
                self.assertEqual(0, zero_gate(data_input)), "failed 'zero' test"

    def test_one(self):
        data_input = (0, 1, 1)
        one = BinaryOperation(name='one')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                one_gate = BinaryGate(indices=(i, j), operation=one)
                self.assertEqual(1, one_gate(data_input)), "failed 'one' test"

    def test_and(self):
        data_input = (0, 1, 1)
        and_op = BinaryOperation(name='and')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                a, b = data_input[i], data_input[j]
                and_gate = BinaryGate(indices=(i, j), operation=and_op)
                self.assertEqual(a & b, and_gate(data_input)), "failed 'and' test"

    def test_or(self):
        data_input = (0, 1, 1)
        or_op = BinaryOperation(name='or')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                a, b = data_input[i], data_input[j]
                or_gate = BinaryGate(indices=(i, j), operation=or_op)
                self.assertEqual(a | b, or_gate(data_input)), "failed 'or' test"

    def test_xor(self):
        data_input = (0, 1, 1)
        xor = BinaryOperation(name='xor')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                a, b = data_input[i], data_input[j]
                xor_gate = BinaryGate(indices=(i, j), operation=xor)
                self.assertEqual(a ^ b, xor_gate(data_input)), "failed 'xor' test"


if __name__ == '__main__':
    unittest.main()
