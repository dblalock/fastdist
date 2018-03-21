#!/bin/env python

# print("------------------------ running tests")

import numpy as np
import unittest

import fastdist as fd
# from fastdist import fastdist as fd

testNum = 0


def passedTest():
    global testNum
    testNum += 1
    print("Passed Test #%d" % testNum)


def assertEqual(a, b):
    print(a, b)
    assert np.allclose(a, b)
    passedTest()


def printVar(varName, var):
    print(varName)
    print(var)


def test_calling_cpp():
    assert fd.swigTest(5) == 6  # cpp should increment arg


def test_array_to_cpp():
    a = np.array((2, 3, 4), 'd')
    assert fd.swigArrayTest(a) == np.sum(a)


# def test_cpp_struct():
#     fd.DistanceMeasureParams(.05, 0)
#     assert True  # initialized struct without throwing


# def test_numpy_to_eigen():
#     A = np.arange(12).reshape((4, 3))
#     rowSums = np.sum(A, axis=1)
#     assert fd.swigEigenTest(A) == np.dot(rowSums, rowSums)


def test_dtw():
    a = np.array((5, 2, 2, 3, 5.1), 'd')
    b = np.array((5, 2, 3, 3, 4), 'd')
    r = 1
    assert np.allclose(fd.dist_dtw(a, b, r), 1.21)  # only last element off


class TestTsClassifier(unittest.TestCase):

    def setUp(self):
        a = np.array((5,2, 2,  3,  5), 'd').reshape((5,1)) # noqa closest DTW
        b = np.array((5,2, 2.5,2.5,5), 'd').reshape((5,1)) # noqa closest L2
        c = np.array((5,2, 2.2,2.9,5), 'd').reshape((5,1)) # noqa closest L1
        self.q = np.array((5,2, 3,  3,  5), 'd').reshape((5,1)) # noqa

        self.tsc = fd.TSClassifier()
        self.aCls = 1
        self.bCls = 2
        self.cCls = 3
        self.tsc.addExample(a, self.aCls)
        self.tsc.addExample(b, self.bCls)
        self.tsc.addExample(c, self.cCls)

    def test_dtw(self):
        self.tsc.setAlgorithm(fd.NN_DTW)
        qCls = self.tsc.classify(self.q)
        assert qCls == self.aCls

    def test_l2(self):
        self.tsc.setAlgorithm(fd.NN_L2)
        qCls = self.tsc.classify(self.q)
        assert qCls == self.bCls

    def test_l1(self):
        self.tsc.setAlgorithm(fd.NN_L1)
        qCls = self.tsc.classify(self.q)
        assert qCls == self.cCls
