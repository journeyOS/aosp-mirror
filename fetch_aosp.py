#  !/usr/bin/env python
#  -*- encoding: utf-8 -*-
#
#  Copyright (c) 2020 anqi.huang@outlook.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import sys

flag = False
host = 'https://github.com'
# host = 'git@github.com'  # 如果使用ssh协议下载，

allLines = sys.stdin.readlines()
for curLine in allLines:
    if curLine.find('wb-break-all') >= 0:
        flag = True
    if flag:
        pos = curLine.find('href="')
        if pos >= 0:
            pos += len('href="')
            last = curLine[pos:]
            end = last.find('"')
            link = last[:end]

            # name to path.
            name = link[link.rfind('/') + 1:]
            prefix = name.find('platform_')
            if prefix >= 0:
                name = name[len('platform_'):]  # ignore platform_
            path = name.replace('_', '/')
            link = host + link
            # print('git clone', link + '.git', path)  # 输出 git clone 命令
            print('git submodule add', link + '.git', path)  # 输出 git submodule add 命令
            flag = False
