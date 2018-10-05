#!/Users/kawahara/.pyenv/shims/python
# -*- coding: utf-8 -*-

u""" stepFunction.py
# ステップ関数とシグモイド関数の実装
# 『ゼロから作るDeepLearning』p.45
# Copyright (C) 2018 J.Kawahara
# 2018.10.5 J.Kawahara 新規作成
"""

import numpy as np
import matplotlib.pylab as plt


def step_function_basic(x):
    u"""
    # ステップ関数
    #
    # 引数xに配列が渡された場合に対応できない
    #
    """

    if x > 0:
        return 1
    else:
        return 0


def step_function_(x):
    u"""
    # ステップ関数
    #
    # 引数xが配列であっても対応可能
    """

    y = x > 0
    return y.astype(np.int)


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    u"""
    # シグモイド関数
    """
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)
plt.plot(x, y1, label="sigmoid")
plt.plot(x, y2, linestyle="--", label="step")
plt.ylim(-0.1, 1.1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("step function & sigmoid function")
plt.legend()
plt.show()
