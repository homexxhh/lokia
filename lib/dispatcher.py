#-*— coding:UTF-8 -*-
#/usr/bin/env python
"""
module descript
"""
import xml.etree.ElementTree as ET

from django.utils.encoding import smart_str
from django.http import HttpResponse

from utils import parse_msg_xml


class DispatcherMiddleware(object):
    def process_request(self, request):
        if request.path_info == "/":
            if request.method == 'GET':
                request.path_info = '/check_signature/'
                return None
            elif request.method == 'POST':
                raw_str = smart_str(request.body)
                msg = parse_msg_xml(ET.fromstring(raw_str))
                msg_type = msg['MsgType']
                path_info = '/' + msg_type + '/'
                if msg_type == 'event':
                    path_info += msg['Event']
                    path_info += '/'
                    if 'EventKey' in msg:
                        path_info += msg['EventKey']
                        path_info += '/'
                request.path_info = path_info
                return None
        else:
            return None