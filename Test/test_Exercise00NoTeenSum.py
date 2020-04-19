from unittest import TestCase
from Exercise00NoTeenSum import Exercise00NoTeenSum


class TestExercise00(TestCase):
    def setUp(self):
        # Normal
        self.normal_00 = Exercise00NoTeenSum()
        self.normal_01 = Exercise00NoTeenSum(0, 1, 2)
        self.normal_02 = Exercise00NoTeenSum(1, 2, 3)
        self.normal_03 = Exercise00NoTeenSum(-1, -2, 3)
        self.normal_04 = Exercise00NoTeenSum(-15, -5, 10)

        # contain value 15/16/both
        self.containExcept_01 = Exercise00NoTeenSum(1, 2, 15)
        self.containExcept_02 = Exercise00NoTeenSum(1, 2, 16)
        self.containExcept_03 = Exercise00NoTeenSum(2, 15, 2)
        self.containExcept_04 = Exercise00NoTeenSum(15, 16, 2)

        # contain teen number
        self.containTeenNum_01 = Exercise00NoTeenSum(2, 1, 14)
        self.containTeenNum_02 = Exercise00NoTeenSum(2, 13, 1)
        self.containTeenNum_03 = Exercise00NoTeenSum(2, 1, 17)
        self.containTeenNum_04 = Exercise00NoTeenSum(17, 1, 2)
        self.containTeenNum_05 = Exercise00NoTeenSum(5, 17, 18)

        # contain 15/16/both and teen number
        self.exceptAndTeen_01 = Exercise00NoTeenSum(16, 17, 18)
        self.exceptAndTeen_02 = Exercise00NoTeenSum(15, 15, 19)
        self.exceptAndTeen_03 = Exercise00NoTeenSum(15, 19, 16)
        self.exceptAndTeen_04 = Exercise00NoTeenSum(17, 18, 16)

        # all numbers is teen
        self.allTeenNums01 = Exercise00NoTeenSum(17, 19, 18)
        self.allTeenNums02 = Exercise00NoTeenSum(17, 18, 19)


class TestNoTeenSum(TestExercise00):
    def testNormalCase(self):
        self.assertEqual(self.normal_00.no_teen_sum(), 0)
        self.assertEqual(self.normal_01.no_teen_sum(), 3)
        self.assertEqual(self.normal_02.no_teen_sum(), 6)
        self.assertEqual(self.normal_03.no_teen_sum(), 0)
        self.assertEqual(self.normal_04.no_teen_sum(), -10)

    def testContainExcept(self):
        self.assertEqual(self.containExcept_01.no_teen_sum(), 18)
        self.assertEqual(self.containExcept_02.no_teen_sum(), 19)
        self.assertEqual(self.containExcept_03.no_teen_sum(), 19)
        self.assertEqual(self.containExcept_04.no_teen_sum(), 33)

    def testContainTeenNums(self):
        self.assertEqual(self.containTeenNum_01.no_teen_sum(), 3)
        self.assertEqual(self.containTeenNum_02.no_teen_sum(), 3)
        self.assertEqual(self.containTeenNum_03.no_teen_sum(), 3)
        self.assertEqual(self.containTeenNum_04.no_teen_sum(), 3)
        self.assertEqual(self.containTeenNum_05.no_teen_sum(), 5)

    def testContainExceptAndTeen(self):
        self.assertEqual(self.exceptAndTeen_01.no_teen_sum(), 16)
        self.assertEqual(self.exceptAndTeen_02.no_teen_sum(), 30)
        self.assertEqual(self.exceptAndTeen_03.no_teen_sum(), 31)
        self.assertEqual(self.exceptAndTeen_04.no_teen_sum(), 16)

    def testAllTeenNumbers(self):
        self.assertEqual(self.allTeenNums01.no_teen_sum(), 0)
        self.assertEqual(self.allTeenNums02.no_teen_sum(), 0)


class TestFixValue(TestCase):
    def setUp(self) -> None:
        self.noTeenSum = Exercise00NoTeenSum()

    def testNormalCase(self):
        self.assertEqual(self.noTeenSum.fix_value(0), 0)
        self.assertEqual(self.noTeenSum.fix_value(1), 1)
        self.assertEqual(self.noTeenSum.fix_value(10), 10)
        self.assertEqual(self.noTeenSum.fix_value(12), 12)
        self.assertEqual(self.noTeenSum.fix_value(-1), -1)
        self.assertEqual(self.noTeenSum.fix_value(-10), -10)
        self.assertEqual(self.noTeenSum.fix_value(20), 20)

    def testExcept(self):
        self.assertEqual(self.noTeenSum.fix_value(15), 15)
        self.assertEqual(self.noTeenSum.fix_value(16), 16)

    def testTeenNum(self):
        self.assertEqual(self.noTeenSum.fix_value(13), 0)
        self.assertEqual(self.noTeenSum.fix_value(14), 0)
        self.assertEqual(self.noTeenSum.fix_value(17), 0)
        self.assertEqual(self.noTeenSum.fix_value(18), 0)
        self.assertEqual(self.noTeenSum.fix_value(19), 0)
