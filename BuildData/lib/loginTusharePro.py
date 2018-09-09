#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: JohnEast

import tushare as ts

def login():
    ts.set_token('d7e28c79162bc5a6fd505e5183c7d9fe45ef6fb84c2eef01b8b25bf5')
    pro = ts.pro_api()
    return pro