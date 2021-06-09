# Python Template for Flow Plugin

This is a framework template for developing Flow Launcher plugins in Python.

It logically breaks the code down into components and also includes tools to
generate plugin information, test locally, and to allow for langauge localisation.

It is not mandatory to use this template,
however doing so helps standardize Python plugins and may assist in debugging.

## :bookmark: Versions

- [Flow](https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/master)
- [Wox](https://github.com/Flow-Launcher/Flow.Launcher.Plugin.PythonTemplate/tree/wox)

## :pushpin: Requirements

- [`flowlauncher`](https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python) Flow's jsonRPC API for Python. It's **NECESSARY** for plugin.
- `python-dotenv` User's config package.

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

The following is some more detail on the important files.

### :snake: Script File

#### main.py

The Python entry point to your plugin (depend on `plugin.json`).

You **shouldn't** have to edit this file.

#### test.py

A file that calls the Flowlauncher query via `main.py` and displays
the results on the command line so you can **debug**.

This file is for developing and doesn't need to be packaged with the plugin.

#### extensions.py

There is a example to show how to use the **3rd package**.

Currently used for `localization` and shouldn't need to be edited unless
you change where the localization files are stored.

#### settings.py

Edit this file to add in information for your plugin that is used throughout the code.

Also uses `dotenv` to load the `.env` file for localization.

#### templates.py

Comes with templates for the JSON RPC query result and action.

Other templates can be added here as you need them.

#### ui.py

The interaction with the Flow Launcher JSON RPC happens here.

The `query` function will have your main query logic.

Most of your code and development will happen in this file and `utils.py`.

#### utils.py

`ui.py` should only hold the UI logic to keep the main thought simple.

`utils.py` could finish other function.

#### :computer: commands.py

This template uses `click` to parse the command line arguments for
the different functions that `commands.py` can perform.

##### gen-plugin-info

Using Example:

```python
python commands.py gen-plugin-info
```

We can use the `commands.py` to update `plugin.json` using
the variables from the package itself.

These are imported from `settings.py` in the **plugin** folder.

##### :globe_with_meridians: Localization Commands

The next few functions allow you to use localization to translate strings
in your plugin to different languages.

You are not required to cater for more than one language but
Flow Launcher is used around the world and many users appreciate being able to
use it in their own language.

If you need help translating to a language, try posting a request on the [Discord](https://discord.gg/AvgAQgh).

###### init

Using Example:

```python
python commands.py init lang
```

Using `gettext` in your code you can integrate localization functionality.

The [gettext documentation](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules)
helps explain this but essentially you wrap any string with
the default gettext tag (underscore and brackets) and
the functions below will know to extract these out to be translated.

For example:

Regular string

```python
self.sendNormalMess(f"Error - {my_err_string}", "Check documentation for accepted units")
```

Adding `gettext` tags to be able to translate both strings

```python
self.sendNormalMess(_(f"Error - {my_err_string}"), _("Check documentation for accepted units"))
```

We can initialize a language (en, zh, es, etc.) using the init function.

This uses `babel.cfg` to know where and which files to search for the `gettext` strings.

This will add these strings to a special text file `messages.po` for each language
in the **translations** folder.

You can then edit this file to add in the specific string translations for that specific language.

###### update

Using Example:

```python
python commands.py update
```

When you update your code, use this function to update the localization strings.

###### compile

Using Example:

```python
python commands.py compile
```

Before shipping the plugin, we need to compile the `.po` file to a `.mo` file for
each langauge with the compile function.

### :package: Package File

#### requirements.txt

The Python package requirements for your plugin.

Currently the user needs to manually install these
once they have installed the plugin as Flow does no Python package management.

The easiest way to do this is for the user to run.

Using Example:

```powershell
pip install -r requirements.txt
```

#### plugin.json

The file that Flow uses to incorporate your plugin to the plugin manifest list.

See [commands.py](#computer-commandspy).

### :wrench: Config File

#### .env

The user config file.

You could change another name sound good for the **User**.

Currently sets the language for the plugin.

The user will need to manually edit this once the plugin is installed to change the language.

If you have localized the plugin,please see [commands.py](#computer-commandspy).

#### babel.cfg

Babel config file showing where to look for strings that can be translated.

### :globe_with_meridians: Localization

These are your localization folders for each langauge your plugin supports.

`plugin\translations\[LANGUAGE]\LC_MESSAGES`

The template comes with English (US) and Chinese but
you can add as many as you would like to support.

The `po` and the `mo` files are described above.

## :runner: ToDos

- [x] auto commands
- [x] local language
- [ ] inputs parser, for multiple inputs
- [ ] setting ui for Flow
