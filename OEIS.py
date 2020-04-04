#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2020-04-03 21:55:38
    @project      : OEIS sequence
    @version      : 1.0
    @source file  : OEIS.py

============================
"""
from sympy import *
class OEIS():
    """docstring for OEIS"""
    def __init__(self):
        super(OEIS, self).__init__()
    def A000108Catalan(self,n=20):
        """
        docstring for A000108Catalan
        a(n) = C(2n,n)/(n+1)
        """
        res = [1]
        for i in range(1,n):
            num = res[-1]*2*(2*i-1)//((i+1))
            res.append(num)
        # print(res)

        total = Integer(0)
        for i,j in enumerate(res):
            total += j/2**(2*i+1)
        print(total)

        return res 

    def test(self):
        """
        docstring for test
        """
        self.A000108Catalan(n=5000)
        return

oeis = OEIS()
oeis.test()



        