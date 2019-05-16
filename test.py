# -*- coding: utf-8 -*-
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
path = 'G:/web-admin/admin\static\css/'
new_path = path[0:-1]
print(new_path)
a = path.split('\\')[1:]
print(a)
path = '/home'
for file in a:
    path += '/' + file
# b = os.path.join('a', *a)
print(path)
