# coding: utf-8


class MulLayer:
    u"""
    乗算レイヤ
    """
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x, y):
        u"""
        順伝播

        x, y の2つの引数を受け取り、それらを乗算して出力する
        """
        self.x = x
        self.y = y
        out = x * y
        
        return out
    
    def backward(self, dout):
        u"""
        逆伝播

        上流から伝わって来た微分（dout）に対して、
        順伝播のひっくり返した値を乗算して下流に流す
        """
        dx = dout * self.y      # x と y をひっくり返す
        dy = dout * self.x

        return dx, dy


class AddLayer:
    u"""
    加算レイヤ
    """
    def __init(self):
        pass

    def forward(self, x, y):
        out = x + y;
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

