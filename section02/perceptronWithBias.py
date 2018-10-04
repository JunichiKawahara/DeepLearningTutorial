#!/Users/kawahara/.pyenv/shims/python
# -*- coding: utf-8 -*-

u""" perceptronWithBias.py
# パーセプトロンの実装 重みとバイアスの導入
# 『ゼロから作るDeepLearning』p.27
# Copyright (C) 2018 J.Kawahara
# 2018.10.3 J.Kawahara 新規作成
"""

import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0

    return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0

    return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0

    return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


print("0 AND 0 = " + str(AND(0, 0)))
print("1 AND 0 = " + str(AND(1, 0)))
print("0 AND 1 = " + str(AND(0, 1)))
print("1 AND 1 = " + str(AND(1, 1)))

print("0 NAND 0 = " + str(NAND(0, 0)))
print("1 NAND 0 = " + str(NAND(1, 0)))
print("0 NAND 1 = " + str(NAND(0, 1)))
print("1 NAND 1 = " + str(NAND(1, 1)))

print("0 AND 0 = " + str(OR(0, 0)))
print("1 AND 0 = " + str(OR(1, 0)))
print("0 AND 1 = " + str(OR(0, 1)))
print("1 AND 1 = " + str(OR(1, 1)))

print("0 XOR 0 = " + str(XOR(0, 0)))
print("1 XOR 0 = " + str(XOR(1, 0)))
print("0 XOR 1 = " + str(XOR(0, 1)))
print("1 XOR 1 = " + str(XOR(1, 1)))
