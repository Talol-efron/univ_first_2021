# -*- coding: utf-8 -*-

import unittest


def plus(x, y):
    return x+y


def minus(x, y):
    return x-y


class Tester(unittest.TestCase):
    def testPlus(self):

        self.assertEqual(plus(1, 2), 3)     # plus(1,2) == 3
        self.assertEqual(plus(10, 20), 30)  # plus(10,20) == 30

        self.assertAlmostEqual(plus(0.3, 0.2), 0.5)  # 0.3+0.2 が大体0.5に等しい

    def testMinus(self):

        self.assertEqual(minus(3, 2), 1)


if __name__ == "__main__":
    unittest.main()
