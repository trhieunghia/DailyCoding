from unittest import TestCase
from Exercise001_Xyz import Xyz


class TestXyz(TestCase):
    def setUp(self):
        self.case1 = Xyz('xyz')
        self.case2 = Xyz("abcxyz")
        self.case3 = Xyz("xyzabc")
        self.case4 = Xyz("12xyz")
        self.case5 = Xyz("abc.xxyz")
        self.case6 = Xyz("abc.xyzxyz")

        self.case7 = Xyz("")
        self.case8 = Xyz("x")
        self.case9 = Xyz("xy")
        self.case10 = Xyz("abxy")
        self.case11 = Xyz(".xyz")
        self.case12 = Xyz("abc.xyz")
        self.case13 = Xyz("12.xyz")
        self.case14 = Xyz("1.xyz.xyz2.xyz")


class TestIsSubString(TestXyz):
    def testNormal(self):
        self.assertEqual(self.case1.xyz_there(), True)
        self.assertEqual(self.case2.xyz_there(), True)
        self.assertEqual(self.case3.xyz_there(), True)
        self.assertEqual(self.case4.xyz_there(), True)
        self.assertEqual(self.case5.xyz_there(), True)
        self.assertEqual(self.case6.xyz_there(), True)

        self.assertEqual(self.case7.xyz_there(), False)
        self.assertEqual(self.case8.xyz_there(), False)
        self.assertEqual(self.case9.xyz_there(), False)
        self.assertEqual(self.case10.xyz_there(), False)
        self.assertEqual(self.case11.xyz_there(), False)
        self.assertEqual(self.case12.xyz_there(), False)
        self.assertEqual(self.case13.xyz_there(), False)
        self.assertEqual(self.case14.xyz_there(), False)
