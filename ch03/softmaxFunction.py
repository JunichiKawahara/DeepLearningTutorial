#!/Users/kawahara/.pyenv/shims/python
# -*- coding: utf-8 -*-

u""" softmaxFunction.py
# ステップ関数とシグモイド関数の実装
# 『ゼロから作るDeepLearning』p.69
# Copyright (C) 2018 J.Kawahara
# 2018.10.5 J.Kawahara 新規作成
"""

import numpy as np
import matplotlib.pylab as plt


def sortmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)   # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
