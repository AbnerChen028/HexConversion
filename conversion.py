# -*- coding:utf-8 -*-

import sys, re
from workflow import Workflow

def converison(wf):

    args = wf.args
    scale = int(args[0])
    number = args[1]

    if not match_result(number, scale):
        wf.add_item(u"数据格式错误")
        wf.send_feedback()
        return

    int_num = int(number, scale)

    bin_title = str(bin(int_num)).replace("0b", "", 1)
    wf.add_item(title=bin_title, subtitle=u"2进制", arg=bin_title, valid=True)

    oct_title = str(oct(int_num)).replace("0", "", 1)
    wf.add_item(title=oct_title, subtitle=u"8进制", arg=oct_title, valid=True)

    int_title = str(int(int_num))
    wf.add_item(title=int_title, subtitle=u"10进制", arg=int_title, valid=True)

    hex_title = str(hex(int_num)).replace("0x", "", 1)
    wf.add_item(title=hex_title, subtitle=u"16进制", arg=hex_title, valid=True)

    wf.send_feedback()


def match_result(number, scale):
    if scale == 2:
        return None != (re.match(r'^[0,1]*$', number))
    if scale == 8:
        return None != (re.match(r'^[0-7]*$', number))
    if scale == 10:
        return None != (re.match(r'^[0-9]*$', number))
    if scale == 16:
        return None != (re.match(r'^[0-9A-Fa-f]*$', number))


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(converison))
