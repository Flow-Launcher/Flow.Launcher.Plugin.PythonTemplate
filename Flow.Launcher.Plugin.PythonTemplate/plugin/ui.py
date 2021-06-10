# -*- coding: utf-8 -*-

import copy
from typing import List

from flowlauncher import FlowLauncher

from plugin.templates import *


class Main(FlowLauncher):
    messages_queue = []
    
    def callBackMethodSample(self, **args):
        action = copy.deepcopy(ACTION_TEMPLATE)
        // do what you want to do
        
        return message

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message['Title'] = title
        message['SubTitle'] = subtitle

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, method: str, value: List):
        # information
        message = copy.deepcopy(RESULT_TEMPLATE)
        message['Title'] = title
        message['SubTitle'] = subtitle

        # action
        action = copy.deepcopy(ACTION_TEMPLATE)
        action['JsonRPCAction']['method'] = method
        action['JsonRPCAction']['parameters'] = value
        message['JsonRPCAction'] = action;

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        q = param.strip()

        # Do your job at here.
        ...

        return self.messages_queue
