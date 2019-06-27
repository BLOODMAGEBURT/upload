# -*- coding: utf-8 -*-
# !/usr/bin/env python
# coding: utf-8
import os

import paramiko

"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       Administrator
   date：          2019/5/16 0016
-------------------------------------------------
   Change Activity:
                   2019/5/16 0016:
-------------------------------------------------
"""

hostname = '192.168.1.145'
username = 'root'
password = '123456'
port = 22


def upload(local_dir, remote_dir):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # print('upload file start %s ' % datetime.datetime.now())

        for root, dirs, files in os.walk(local_dir):
            # print(99, '[%s][%s][%s]' % (root, dirs, files))
            for filepath in files:
                local_file = os.path.join(root, filepath)
                # print(11, '[%s][%s][%s][%s]' % (root, filepath, local_file, local_dir))
                a = local_file.replace(local_dir, '').replace('\\', '/').lstrip('/')
                # print('01', a, '[%s]' % remote_dir)
                remote_file = os.path.join(remote_dir, a)
                # print(22, remote_file)
                try:
                    sftp.put(local_file, remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                    # print("66 upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                # print(0, local_path, local_dir)
                remote_path = remote_dir[0:-1]
                # print(1, remote_path)
                path = local_path.split('\\')[1:]
                for directory in path:
                    remote_path += '/' + directory
                # print(33, remote_path)
                try:
                    sftp.mkdir(remote_path)
                    print(44, "mkdir path %s" % remote_path)
                except Exception as e:
                    print(55, e)
        # print('77,upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(88, e)


if __name__ == '__main__':
    # local_dir = 'E:/dist'  # 本地需要上传的文件所处的目录,最后不要带斜杠
    path = os.getcwd()  # 获取当前路径
    # print('path:{}'.format(path))
    local_dir = os.path.join(path, 'dist').replace('\\', '/')    # 当前路径  拼接 dist 文件夹, 转换路径符号
    # print('local_dir:{}'.format(local_dir))
    # remote_dir = '/home/data/www/saaspro/public/admin/'  # linux下目录，最后必须带斜杠
    remote_dir = '/home/test/admin/'  # linux下目录，最后必须带斜杠

    upload(local_dir, remote_dir)
