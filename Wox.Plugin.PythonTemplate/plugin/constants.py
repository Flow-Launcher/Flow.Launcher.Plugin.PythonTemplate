# -*- coding: utf-8 -*-


import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


ICON_PATH = 'assets/favicon.ico'

# The default value can work, if no user config.
CONFIG = os.getenv('CONFIG', 'default config')
