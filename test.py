# -*- coding: utf-8 -*-
import os
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       Administrator
   date：          2019/5/16 0016
-------------------------------------------------
   Change Activity:
                   2019/5/16 0016:
-------------------------------------------------
"""
path = os.getcwd()
print('path:{}'.format(path))
abs_path = os.path.join(path, 'dist')
print('abs_path:{}'.format(abs_path))
a = path.split('\\')[1:]
print(a)
path = '/home'
for file in a:
    path += '/' + file
# b = os.path.join('a', *a)
print(path)
