#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'zhangzz'

def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception,e:
        arg = default
    return arg