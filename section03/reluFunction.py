#!/Users/kawahara/.pyenv/shims/python
# -*- coding: utf-8 -*-

u""" reluFunction.py
# ReLU関数の実装
# 『ゼロから作るDeepLearning』p.52
# Copyright (C) 2018 J.Kawahara
# 2018.10.5 J.Kawahara 新規作成
"""

import numpy as np
import matplotlib.pylab as plt


def relu(x):
    u"""
    # ReLU (Rectified Linear Unit)
    #
    # 入力が0を超えていれば、その入力をそのまま出力する。
    # 入力が0以下ならば0を出力する。
    """

    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y, label="ReLU")
plt.ylim(-0.1, 1.1)
plt.title("ReLU")
plt.show()
