# -*- coding: utf-8 -*-


import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dotenv_path = os.path.join(basedir, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


ICON_PATH = 'assets/favicon.ico'

# The default value can work, if no user config.
CONFIG = os.getenv('CONFIG', 'default config')
LOCAL = os.getenv("local", "en")


# the information of package
__package_name__ = "Plugin"
__version__ = "0.0.1"
__short_description__ = "DESCRIPTION"
GITHUB_USERNAME = "USERNAME"


readme_path = os.path.join(basedir, 'README.md')
try:
    __long_description__ = open(readme_path, "r").read()
except:
    __long_description__ = __short_description__


# other information
PLUGIN_ID = "uuid"
ICON_PATH = "assets/favicon.ico"
PLUGIN_ACTION_KEYWORD = "KEYWORD"
PLUGIN_AUTHOR = "AUTHOR_NAME"
PLUGIN_PROGRAM_LANG = "python"
PLUGIN_URL = f"https://github.com/{GITHUB_USERNAME}/{__package_name__}"
PLUGIN_EXECUTE_FILENAME = "main.py"
