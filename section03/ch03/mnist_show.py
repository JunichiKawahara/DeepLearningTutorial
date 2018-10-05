#!/Users/kawahara/.pyenv/shims/python
# -*- coding: utf-8 -*-

u""" mnist_show.py
# MNIST画像を表示してみる
# 『ゼロから作るDeepLearning』p.74
# Copyright (C) 2018 J.Kawahara
# 2018.10.5 J.Kawahara 新規作成
"""

import numpy as np
from mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
