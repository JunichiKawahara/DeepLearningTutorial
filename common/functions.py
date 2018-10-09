# coding: utf-8
import numpy as np

u""" functions.py
# 汎用的に使用する関数の定義
# 『ゼロから作るDeepLearning』
# Copyright (C) 2018 J.Kawahara
# 2018.10.8 J.Kawahara 新規作成
"""


def identity_function(x):
    u"""
    恒等関数（入力をそのまま出力する）
    回帰問題の出力層で主に使用される
    """
    return x


def softmax(x):
    u"""
    ソフトマックス関数
    分類問題の出力層で主に使用される
    """
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x)   # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))


def step_function(x):
    u"""
    階段関数
    """
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    u"""
    シグモイド関数
    """
    return 1 / (1 + np.exp(-x))


def mean_squared_error(y, t):
    u"""
    2乗和誤差
    損失関数として用いられる
    """
    return 0.5 * np.sum((y + t) ** 2)


def cross_entropy_error(y, t):
    u"""
    交差エントロピー誤差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換する
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def numerical_diff(f, x):
    u"""
    数値微分
    """
    h = 1e-4    # 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)

