# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv

from plugin import Main

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == "__main__":
    r = Main().query('')
    print(r)
