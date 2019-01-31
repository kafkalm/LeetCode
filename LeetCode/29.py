#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 29.py
@time: 2019/1/30 030 16:24
@desc:给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
'''

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    out = 0
    if dividend == 0:
        return 0
    if dividend <0 and divisor<0:
        while dividend <= 0:
            out = out + 1
            dividend = dividend - divisor
        out = out - 1
    elif dividend<0 and divisor>0:
        while dividend <= 0:
            out = out - 1
            dividend = dividend + divisor
        out = out + 1
    elif dividend >0 and divisor>0:
        while dividend >= 0:
            out = out + 1
            dividend = dividend - divisor
        out = out - 1
    elif dividend >0 and divisor<0:
        while dividend >= 0:
            out = out - 1
            dividend = dividend + divisor
        out = out + 1
    if (-2)**31 < out < 2**31 -1:
        return out
    else:
        return 2**31-1


def divide(dividend, divisor):
    """
    使用指数移位来计算
    :param dividend:
    :param divisor:
    :return:
    """
    # 1 符号相同 -1 符号不同
    f = 1
    f_1 = str(dividend)[0]
    f_2 = str(divisor)[0]
    out = 0
    offset = 0
    init_divisor = divisor
    if dividend == 0:
        return 0
    if (f_1 == '-' and f_2 != '-') or (f_1 != '-' and f_2 == '-'):
        f = -1
    if f == 1:
        if f_1 == '-':
            while dividend <= 0:
                if dividend - (divisor<<1) >= 0:
                    out = out - ((divisor<<1) +dividend-(divisor<<1))
                    break
                divisor = divisor << 1
                offset += 1
                dividend -= divisor
                out += (1<<offset)
        else:
            while dividend >= 0:
                if dividend - (divisor<<1) <= 0:
                    out = out + divide(dividend,init_divisor)
                    break
                divisor = divisor << 1
                offset += 1
                dividend -= divisor
                out += (1<<offset)
    else:
        if f_1 == '-':
            while dividend <= 0:
                if dividend + (divisor<<1) >= 0:
                    out = out + ((divisor << 1) + dividend - (divisor << 1))
                    break
                divisor = divisor << 1
                offset += 1
                dividend += divisor
                out -= (1<<offset)
        else:
            while dividend >= 0:
                if dividend + (divisor<<1) <= 0:
                    out = out - ((divisor << 1) + dividend - (divisor << 1))
                    break
                divisor = divisor << 1
                offset += 1
                dividend += divisor
                out -= (1<<offset)
    if (-2)**31 < out < 2**31 -1:
        return out
    return 2**31 - 1


def divide(dividend, divisor):

    #符号位
    sign = (dividend > 0) is (divisor > 0)

    dividend, divisor = abs(dividend), abs(divisor)

    res = 0

    #先利用移位 扩大除数 然后再利用移位逐渐缩小除数
    while (dividend >= divisor):
        tmp, i = divisor, 1
        n = 8
        while (dividend >= tmp):
            dividend -= tmp
            res += i

            tmp = tmp << n
            i = i << n
        n = n >> 3

    if not sign:
        res = -res

    return min(max(-2147483648, res), 2147483647)

dividend = 10000
divisor = 2
sign = (dividend > 0) is (divisor > 0)
print(sign)
print(divide(dividend,divisor))