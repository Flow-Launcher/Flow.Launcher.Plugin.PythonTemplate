# Python Template for Flow Plugin

This is a framework template for developing Flow Launcher plugins in Python. It logically breaks the code down into components and also includes tools to generate plugin information, test locally, and to allow for langauge localisation.

It is not mandatory to use this template, however doing so helps standardize Python plugins and may assist in debugging.

## :bookmark: Versions

- [Flow](https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/master)
- [Wox](https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/wox)

## :file_folder: File Structure

```
.
│  README.md
│  LICENSE
│  plugin.json
│  .gitignore
│  .env
│  main.py
│  test.py
|  commands.py
│  requirements.txt
|  requirements-dev.txt
|  babel.cfg
│
├─assets
│      example.png
│      favicon.ico
│
└─plugin  # main scripts
        __init__.py
        extensions.py
        settings.py
        templates.py
        ui.py
        utils.py
        └──translations  # localization
                ├─en_US
                └─zh_CN
```

## :open_file_folder: README.md

The Github README markdown file for your plugin project.

## :open_file_folder: LICENSE

Update this file to outline the license for your plugin.

## :open_file_folder: plugin.json

The file that Flow uses to incorporate your plugin to the plugin manifest list. See [https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/master#commands.py].

## :open_file_folder: .gitignore

Files for git to ignore when merging changes.

## :open_file_folder: .env

User config file. Currently sets the language for the plugin. The user will need to manually edit this once the plugin is installed to change the language (if you have localized the plugin. See [https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/master#commands.py]).

## :open_file_folder: main.py

The Python entry point to your plugin. You shouldn't have to edit this file.

## :open_file_folder: test.py

A file that calls the Flowlauncher query via `main.py` and displays the results on the command line so you can debug. This file is for developing and doesn't need to be packaged with the plugin.

## :open_file_folder: commands.py

This template uses the Python `click` package to parse the command line arguments for the different functions that `commands.py` can perform..

Those functions are:

### gen-plugin-info

```python
python commands.py gen-plugin-info
```

We can use the `commands.py` to update `plugin.json` using the variables from the package itself. These are imported from `settings.py` in the **plugin** folder.

### init (localization)

```python
python commands.py init lang
```

The next few functions allow you to use localization to translate strings in your plugin to different languages. You are not required to cater for more than one language but Flow Launcher is used around the world and many users appreciate being able to use it in their own language. If you need help translating to a language, try posting a request on the Discord server.

Using `gettext` in your code you can integrate localization functionality.The [gettext documentation](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules) helps explain this but essentially you wrap any string with the default gettext tag (underscore and brackets) and the functions below will know to extract these out to be translated. For example:

Regular string

```python
self.sendNormalMess("Error - {}").format(my_err_string), "Check documentation for accepted units",)
```

Adding `gettext` tags to be able to translate both strings

```python
self.sendNormalMess(_("Error - {}").format(my_err_string), _("Check documentation for accepted units"),)
```

We can initialize a language (en, zh, es, etc.) using the init function. This uses `babel.cfg` to know where and which files to search for the `gettext` strings. This will add these strings to a special text file - `messages.po` for each language in the **translations** folder. You can then edit this file to add in the specific string translations for that specific language.

### update (localization)

```python
python commands.py update
```

When you update your code, use this function to update the localization strings.

### compile (localization)

```python
python commands.py compile
```

Before shipping the plugin, we need to compile the `.po` file to a `.mo` file for each langauge with the compile function.

## :open_file_folder: requirements.txt

The Python package requirements for your plugin. Currently the user needs to manually install these once they have installed the plugin as Flow does no Python package management. The easiest way to do this is for the user to run.

```powershell
pip install -r requirements.txt
```

## :open_file_folder: requirements-dev.txt

Python package requirements for developers of your plugin.

## :open_file_folder: babel.cfg

Babel config file showing where to look for strings that can be translated.

## :open_file_folder: assets\\example.png

The assets folder are for any images, videos, or other assets for your plugin or Github README. In this case `example.png` is the example image for the default `README.md`.

## :open_file_folder: assets\\favicon.png

The icon for your plugin that appears in the query results.

## :open_file_folder: plugin\\\_\_init\_\_.py

The Python file that runs when you initialise the plugin. Pulls in settings and Main function. Code shouldn't need to be edited but you can update the comment to describe the plugin if you like.

## :open_file_folder: plugin\\extensions.py

Currently used for localization and shouldn't need to be edited unless you change where the localization files are stored.

## :open_file_folder: plugin\\settings.py

Edit this file to add in information for your plugin that is used throughout the code. Also uses the Python dotenv package to load the `.env` file for localization.

## :open_file_folder: plugin\\templates.py

Comes with templates for the JSONRPC query result and action. Other templates can be added here as you need them.

## :open_file_folder: plugin\\ui.py

The interaction with the FlowLauncher JSONRPC happens here. The Query function will have your main query logic. Most of your code and development will happen in this file and `utils.py`.

## :open_file_folder: plugin\\utils.py

This Python file will hold all your support functions for your plugin.

## :open_file_folder: plugin\\translations\\\[LANGUAGE\]\\LC_MESSAGES

These are your localization folders for each langauge your plugin supports. The template comes with English (US) and Chinese but you can add as many as you would like to support. The `po` and the `mo` files are described above.

## :pushpin: Requirements

- [`flowlauncher`](https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python) Flow's jsonRPC API for Python. It's **NECESSARY** for plugin.
- `python-dotenv` User's config package.

## :runner: ToDos

- [x] auto commands
- [x] local language
- [ ] inputs parser, for multiple inputs
- [ ] setting ui for Flow
