#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 12.py
@time: 2019/1/29 029 14:44
@desc:数字转罗马字符
'''
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    out = {}
    if num // 1000:
        thousand = num // 1000
        out['thousand'] = thousand*dic[1000]
        left = num % 1000
        if left // 100:
            hundred = left // 100
            if hundred == 9:
                out['hundred'] = dic[900]
            elif hundred >=5:
                out['hundred'] = dic[500]+(hundred-5)*dic[100]
            elif hundred == 4:
                out['hundred'] = dic[400]
            else:
                out['hundred'] = hundred*dic[100]
            left = left % 100
        if left // 10:
            ten = left // 10
            if ten == 9:
                out['ten'] = dic[90]
            elif ten >= 5:
                out['ten'] = dic[50] + (ten - 5) * dic[10]
            elif ten == 4:
                out['ten'] = dic[40]
            else:
                out['ten'] = ten * dic[10]
            left = left % 10
        if left:
            g = left
            if g == 9:
                out['g'] = dic[9]
            elif g >=5:
                out['g'] = dic[5] + (g - 5) * dic[1]
            elif g == 4:
                out['g'] = dic[4]
            else:
                out['g'] = g * dic[1]
    elif num // 100:
        hundred = num // 100
        if hundred == 9:
            out['hundred'] = dic[900]
        elif hundred >= 5:
            out['hundred'] = dic[500] + (hundred - 5) * dic[100]
        elif hundred == 4:
            out['hundred'] = dic[400]
        else:
            out['hundred'] = hundred * dic[100]
        left = num % 100
        if left // 10:
            ten = left // 10
            if ten == 9:
                out['ten'] = dic[90]
            elif ten >= 5:
                out['ten'] = dic[50] + (ten - 5) * dic[10]
            elif ten == 4:
                out['ten'] = dic[40]
            else:
                out['ten'] = ten * dic[10]
            left = left % 10
        if left:
            g = left
            if g == 9:
                out['g'] = dic[9]
            elif g >=5:
                out['g'] = dic[5] + (g - 5) * dic[1]
            elif g == 4:
                out['g'] = dic[4]
            else:
                out['g'] = g * dic[1]
    elif num // 10:
        ten = num // 10
        if ten == 9:
            out['ten'] = dic[90]
        elif ten >= 5:
            out['ten'] = dic[50] + (ten - 5) * dic[10]
        elif ten == 4:
            out['ten'] = dic[40]
        else:
            out['ten'] = ten * dic[10]
        left = num % 10
        if left:
            g = left
            if g == 9:
                out['g'] = dic[9]
            elif g >= 5:
                out['g'] = dic[5] + (g - 5) * dic[1]
            elif g == 4:
                out['g'] = dic[4]
            else:
                out['g'] = g * dic[1]
    else:
        g = num
        if g == 9:
            out['g'] = dic[9]
        elif g >= 5:
            out['g'] = dic[5] + (g - 5) * dic[1]
        elif g == 4:
            out['g'] = dic[4]
        else:
            out['g'] = g * dic[1]

    output = out.get('thousand','')+out.get('hundred','')+out.get('ten','')+out.get('g','')
    return output

print(intToRoman(1001))
