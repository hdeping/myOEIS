#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2020-04-02 23:13:06
    @project      : Bowl's Sequence
    @version      : 1.0
    @source file  : code.py

============================
"""
from sympy import *

class Bowl():
    """docstring for Bowl"""
    def __init__(self):
        super(Bowl, self).__init__()
    def getFactorials(self,n):
        """
        docstring for getFactorials
        n:
            integer
        return:
            [1!,2!,...,n!]
        """
        res = []
        num = 1 
        for i in range(1,n+1):
            num = num*i 
            res.append(num)

        return res
    def testBowl(self,n=100):
        """
        docstring for testArctanSqrt

        f\left(x\right)&=&\arctan\left(1-\sqrt{1-x^{2}}\right)

        """
        paras = [Integer(1),Integer(1)/2]
        for i in range(n):
            num = paras[-1]*(2*i+2)*(2*i+1)
            num = num /(4*(i+2)*(i+1))
            paras.append(num)
        # print(paras)

        # get all of b
        b = []
        b.append(paras[0])
        b.append(-paras[1])
        for i in range(2,n+2):
            num = paras[i-1] - 3*paras[i]
            b.append(num)

        # prepare all of the factorials
        factorials = self.getFactorials(2*n+1)
        factorials = [1] + factorials

        res = [1]
        factors = []
        # for i in tqdm(range(1,n)):
        print(1,1,1,2)
        for i in range(1,n):
            num = 0
            for k in range(i):
                # print("k = ",k,res[k],b[i-k])
                num += res[k]*b[i-k]/factorials[2*k+1]

            p,q = fraction(-num/(2*i+2))
            num = -num*factorials[2*i+1]
            res.append(num)
            print(i+1,self.getFactorNum(num,5))
            # print("p_{%d} & = & %d \\\\"%(i+1,p))
            # print("q_{%d} & = & %d \\\\"%(i+1,q))
            # dicts = factorint(q)
            # split = ""
            # for key in dicts:
            #     value  = dicts[key]
            #     split += "%d^{%d}\\times"%(key,value)
            # print("& = & %s\\\\"%(split))


        
        return

bowl = Bowl()
bowl.testBowl()