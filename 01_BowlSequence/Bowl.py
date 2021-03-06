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
import numpy as np
from scipy import integrate

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
    def getFactorNum(self,num,factor):
        """
        docstring for getFactorNum
        get the number of a specific factor
        """
        n = 0 
        while num%factor == 0 and num > 0:
            n = n + 1
            num = num // factor
        return n

    def getFactorSplit(self,q):
        """
        docstring for getFactorSplit
        """
        dicts = factorint(q)
        split = ""
        for key in dicts:
            value  = dicts[key]
            split += "%d^{%d}\\times"%(key,value)

        split = split[:-6]
        print("& = & %s\\\\"%(split))
        return split

    def testIntegral(self):
        """
        docstring for testIntegral
        """
        f = lambda x: np.arctan(1-np.sqrt(1-x*x))
        s,err = integrate.quad(f,0,1)
        print(s)

        n = 1
        f = lambda x: np.cos(x)*(1-np.cos(x))**n
        s,err = integrate.quad(f,0,1)
        print(s)

        f = lambda x: np.cos(x)*np.arctan((1-np.cos(x)))
        s,err = integrate.quad(f,0,np.pi/2)
        print(s)
        return
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
        P,Q = [1],[2]
        factors = []
        # for i in tqdm(range(1,n)):
        # print(1,1,1,2)
        n3 = [0]
        n3_residue = [1]
        for i in range(1,n):
            num = 0
            for k in range(i):
                # print("k = ",k,res[k],b[i-k])
                num += res[k]*b[i-k]/factorials[2*k+1]

            p,q = fraction(-num/(2*i+2))
            P.append(p)
            Q.append(q)
            num = -num*factorials[2*i+1]
            res.append(num)
            print(i,len(str(num))/i)
            # n3.append(self.getFactorNum(num,3))
            # n3_residue.append(i+1-n3[-1])
            # print(i+1,n3_residue[-1])
            # print("p_{%d} & = & %d \\\\"%(i+1,p))
            # print("q_{%d} & = & %d \\\\"%(i+1,q))
        # print(n3)
        # print(n3_residue)

        fp = []
        filenames = ["A333691.txt","A333713.txt","A333714.txt"]
        for name in filenames:
            fp.append(open(name,"w"))
        for i,(n,p,q) in enumerate(zip(res,P,Q)):
            fp[0].write("%d %d\n"%(i+1,n))
            fp[1].write("%d %d\n"%(i+1,p))
            fp[2].write("%d %d\n"%(i+1,q))
            # print(i,len(str(p)))

        print(res[1:50])
        print(P[1:50])
        
        return

    def test(self):
        """
        docstring for test
        """
        self.testBowl(n = 1000)
        # self.testIntegral()
        return

bowl = Bowl()
bowl.test()