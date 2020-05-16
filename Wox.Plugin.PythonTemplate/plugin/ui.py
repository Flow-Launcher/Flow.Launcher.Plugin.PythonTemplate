# -*- coding: utf-8 -*-

import copy
from typing import List

from plugin.templates import *
from wox import Wox


class Main(Wox):
    messages_queue = []

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
        message.update(action)

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        q = param.strip()

        # Do your job at here.
        ...

        return self.messages_queue
