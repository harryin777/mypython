# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys

import requests

import time

JOB_URL = sys.argv[1]
JOB_NAME = sys.argv[2]
BUILD_NUMBER = sys.argv[3]
currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/b7ad342c-a0c3-44a3-8018-8b4e7c5bc73c'
method = 'post'
headers = {
    'Content-Type': 'application/json'
}
json = {
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True,
            "enable_forward": True
        },
        "elements": [{
            "tag": "div",
            "text": {
                "content": "项目名称：" + JOB_NAME + "\n构建编号：第" + BUILD_NUMBER + "次构建\n运行时间：" + currenttime,
                "tag": "lark_md"
            }
        }, {
            "actions": [{
                "tag": "button",
                "text": {
                    "content": "查看报告",
                    "tag": "lark_md"
                },
                "url": JOB_URL,
                "type": "default",
                "value": {}
            }],
            "tag": "action"
        }],
        "header": {
            "title": {
                "content": JOB_NAME + " 构建报告",
                "tag": "plain_text"
            }
        }
    }
}
requests.request(method=method, url=url, headers=headers, json=json)