# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 should be InvalidInput')

    def testEquilateralTrianglesD(self):
        self.assertNotEqual(classifyTriangle(3, 3, 4), 'Equilateral', '3,3,4 should not be Equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles', '3,3,4 should be Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4, 3, 4), 'Isoceles', '4,3,4 should be Isoceles')

    def testIsocelesTrianglesC(self):
        self.assertNotEqual(classifyTriangle(3, 2, 4), 'Isoceles', '3,2,4 should not be Isoceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10, 11, 12 should be Scalene')

    def testScaleneTrianglesB(self):
        self.assertNotEqual(classifyTriangle(3, 3, 4), 'Scalene', '3,3,4 should not be Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(100, 3, 4), 'NotATriangle', '100, 3, 4 should be "not a triangle"')

    def testNotATriangleB(self):
        self.assertNotEqual(classifyTriangle(5, 3, 4), 'NotATriangle', '5, 3, 4 should not be "not a triangle"')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(0, 3, 4), 'InvalidInput', '0, 3, 4 should be "InvalidInput"')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
